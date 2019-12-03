import numpy as np

try:
  from subBlock import subBlock
except ImportError:
  from .subBlock import subBlock


class padded:
  def __init__(self, obj, n):
    self.obj = obj
    self.padding = np.zeros(n)

class block:
  def __init__(self, cArr, thinned=True):

    self.thinned = thinned

    self.subBlockSize = 0
    if thinned:
      self.subBlockSize = 39*8*4 #bytes
    else:
      self.subBlockSize = 39*7*4 #bytes


    self.subBlocks = []

    for iSB in range(21):
      start = iSB*self.subBlockSize
      self.subBlocks.append( subBlock(cArr[start:start+self.subBlockSize]) )
          




  def isA(self, cType):
    return 
