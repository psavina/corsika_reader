#===============================================
# runTrailer
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

class runTrailer:
  def __init__(self):
    self.ID = blockID()
    self.runNumber = 0
    self.eventsProcessed = 0
    self.pad = np.zeros(270)
