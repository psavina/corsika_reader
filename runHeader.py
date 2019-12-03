#===============================================
# runHeader
#===============================================
#
#
#===============================================

try:
  from blockID import blockID
except ImportError:
  from .blockID import blockID

try:
  from ioConst import maxObsLevel
except ImportError:
  from .ioConst import maxObsLevel

import numpy as np

class runHeader:
  def __init__(self, words):
    self.ID			= blockID(words.pop(0))
    self.runNumber		= words.pop(0)
    self.dateStart		= words.pop(0)
    self.version		= words.pop(0)
    self.obsLevels		= int(words.pop(0))
    self.obsHeight		= []
    for i in range( self.obsLevels ):
      self.obsHeight.append( words.pop(0) )  # cm
    self.spectralSlope		= words.pop(0)
    self.eMin			= words.pop(0)
    self.eMax			= words.pop(0)
    self.flagEGS4		= words.pop(0)
    self.flagNKG		= words.pop(0)
    self.cutoffHad		= words.pop(0)
    self.cutoffMu		= words.pop(0)
    self.cutoffEl		= words.pop(0)
    self.cutoffPh		= words.pop(0)
    self.constC			= []
    for i in range( 50 ):
      self.constC.append( words.pop(0) )
    self.constUNUSED1a		= []
    for i in range( 5 ):
      self.constUNUSED1a.append( words.pop(0) )
    self.coordinateRotation	= words.pop(0)
    self.constUNUSED1b		= []
    for i in range( 14 ):
      self.constUNUSED1b.append( words.pop(0) )
    self.constUNUSED1b		= []
    for i in range( 14 ):
      self.constUNUSED1b.append( words.pop(0) )
    self.constCKA		= []
    for i in range( 40 ):
      self.constCKA.append( words.pop(0) )
    self.constCETA		= []
    for i in range( 5 ):
      self.constCETA.append( words.pop(0) )
    self.constCSTRBA		= []
    for i in range( 11 ):
      self.constCSTRBA.append( words.pop(0) )
    self.constUNUSED2		= []
    for i in range( 97 ):
      self.constUNUSED2.append( words.pop(0) )
    self.constXscatt		= words.pop(0)
    self.constYscatt		= words.pop(0)
    self.constHLAY		= []
    for i in range( 5 ):
      self.constHLAY.append( words.pop(0) )
    self.constAATM		= []
    for i in range( 5 ):
      self.constAATM.append( words.pop(0) )
    self.constBATM		= []
    for i in range( 5 ):
      self.constBATM.append( words.pop(0) )
    self.constCATM		= []
    for i in range( 5 ):
      self.constCATM.append( words.pop(0) )
    self.constNFLAIN		= words.pop(0)
    self.constNFLDIF		= words.pop(0)
    self.constNFLPI             = words.pop(0)
    self.constNFLPCHE           = words.pop(0)
