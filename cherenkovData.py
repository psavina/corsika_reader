#===============================================
# cherenkovData
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

class cherenkovDataUnthinned:
  def __init__(self):
    self.photonsInBunch = 0
    self.x = 0
    self.y = 0
    self.u = 0
    self.v = 0
    self.t = 0
    self.distance = 0
  
class cherenkovData(cherenkovDataUnthinned):
  def __init__(self):
    super().__init__()
    self.weight = 0
