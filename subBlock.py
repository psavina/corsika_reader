#===============================================
# block
#===============================================
#
#
#===============================================

try:
  from blockID import blockID
except ImportError:
  from .blockID import blockID

try:
  from runHeader import runHeader
except ImportError:
  from .runHeader import runHeader

try:
  from eventHeader import eventHeader
except ImportError:
  from .eventHeader import eventHeader

try:
  from runTrailer import runTrailer
except ImportError:
  from .runTrailer import runTrailer

try:
  from eventTrailer import eventTrailer
except ImportError:
  from .eventTrailer import eventTrailer
  
try:
  from particleData import particleData
except ImportError:
  from .particleData import particleData
  
try:
  from cherenkovData import cherenkovData
except ImportError:
  from .cherenkovData import cherenkovData

try:
  from ioConst import partInBlock
except ImportError:
  from .ioConst import partInBlock

import struct

class subBlock:
  def __init__(self, cArr):
    words = self.char2words( cArr )
    self.data = None
    if words[0] == 'EVTH':
      self.data = eventHeader( words )
    if words[0] == 'RUNH':
      self.data = runHeader( words )
    if words[0] == 'EVTE':
      self.data = eventTrailer( words )
    if words[0] == 'RUNE':
      self.data = runTrailer( words )

    



  

  def char2words(self, cArr):
    words  = []
    firstByte = 0
    if ((cArr[0]   == 'R' and
	 cArr[0+1] == 'U' and
	 cArr[0+2] == 'N' and
	 cArr[0+3] == 'H') or
	(cArr[0]   == 'R' and
	 cArr[0+1] == 'U' and
	 cArr[0+2] == 'N' and
	 cArr[0+3] == 'E') or
	(cArr[0]   == 'E' and
	 cArr[0+1] == 'V' and
	 cArr[0+2] == 'T' and
	 cArr[0+3] == 'H') or
	(cArr[0]   == 'E' and
	 cArr[0+1] == 'V' and
	 cArr[0+2] == 'T' and
	 cArr[0+3] == 'E')):
      word = ''.join(cArr[:4])
      words.append( word )
      firstByte = 4
    for byte in range(firstByte, len(cArr) - 4, 4 ):
      wp = struct.pack( 'cccc',
			cArr[byte],
			cArr[byte+1],
			cArr[byte+2],
			cArr[byte+3])
      wu = struct.unpack( 'f', wp )
      words.extend( wu )
    return words

