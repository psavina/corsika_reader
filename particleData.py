#===============================================
# particleData
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

class particleDataUnthinned:
  def __init__(self):
    self.description = 0
    self.px = 0
    self.py = 0
    self.pz = 0
    self.x = 0
    self.y = 0
    self.tOz = 0

  def isParticle(self):
    p = (0 < self.description and self.description < 100000)
    return p

  def isNucleus(self):
    p = (100000 <= self.description and self.description < 9900000)
    return p

  def isCherenkov(self):
    p = (9900000 <= self.description)
    return p

  
class particleData(particleDataUnthinned):
  def __init__(self):
    super().__init__()
    self.weight = 0
