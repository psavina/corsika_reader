#===============================================
# block
#===============================================
#
#
#===============================================

try:
  from block import block
except ImportError:
  from .block import block

try:
  from corsikaMessage import corsikaMessage
except ImportError:
  from .corsikaMessage import corsikaMessage

import numpy as np
import struct

class rawCorsikaFile:
  def __init__(self, filename):
    self.printer = corsikaMessage(2)
    try:
      self.cFile = open(filename, 'rb')
    except IOError:
      self.printer.ERROR("Error opening Corsika file: "+filename)
      exit(1)

    #------------------------------
    # Search for string 'RUNH' at
    # the beginning of file with
    # a certain offset that is 4
    # in 32 bit linux, but diffe-
    # rent on different systems. If
    # RUNH is not found the file is
    # most certainly corrupt
    #------------------------------

    b = []
    for i in range(20):
      b.extend( self.cFile.read(1) )

    foundRUNH = False
    for i in range(16):
      if (b[i]   == 'R' and
	  b[i+1] == 'U' and
	  b[i+2] == 'N' and
	  b[i+3] == 'H'):
	self.paddingSize = i
	foundRUNH = True

    if(not foundRUNH):
      self.cFile.close()
      self.printer.ERROR('expected RUNH not found')
      exit(1)
    else:
      self.printer.DEBUG('RUNH found at '+str(self.paddingSize))

    self.cFile.seek(0,2)
    self.EOF = self.cFile.tell()
    self.cFile.seek(0)
    self.printer.DEBUG('EOF at '+str(self.EOF))
    self.blocksInDiskBlock = 21
    self.diskBlock = None


    self.currentBlockNumber = 0
    self.diskBlockBuffer = None
    self.indexDiskBlockBuffer = 0
    self.blockBufferValid = False


    #-----------------------------------
    # TODO: this should be optimized
    # These numbers come from a 
    # calculation from a c++ code.
    # It would be preferred to make it
    # estimate from python for possible
    # changes in future
    #----------------------------------
    
    self.unthinnedDiskBlockSize = 22932
    self.thinnedDiskBlockSize = 26208
    
  def next(self, myID):

    status = self.readBlock(True, myID)
    
    return status

  def seek(self, position):
    a = position

  def readBlock(self, thinned, myID):
    size = 0
    if thinned:
      size = self.thinnedDiskBlockSize
    else:
      size = self.unthinnedDiskBlockSize

    sizeDisk = size+2*self.paddingSize
    
    if((self.currentBlockNumber+1)*sizeDisk >= self.EOF):
      self.printer.ERROR("EOF exceeded")
      return False

    self.cFile.seek( myID*sizeDisk+self.paddingSize )

    
    self.diskBlock = block( struct.unpack( size*'c', self.cFile.read(size) ) )
    self.blockBufferValid = True
    return True
    
    
  def close(self):
    self.cFile.close()
    
