#===============================================
# eventTrailer
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

class eventTrailer:
  def __init__(self):
    self.ID = blockID()
    self.eventNumber = 0
    self.photons = 0
    self.electrons = 0
    self.hadrons = 0
    self.muons = 0
    self.particles = 0

    self.lateralX = np.zeros(21)
    self.lateralY = np.zeros(21)
    self.lateralXY = np.zeros(21)
    self.lateralYX = np.zeros(21)

    self.lateral2X = np.zeros(21)
    self.lateral2Y = np.zeros(21)
    self.lateral2XY = np.zeros(21)
    self.lateral2YX = np.zeros(21)

    self.electronNumber = np.zeros(10)
    self.age = np.zeros(10)
    self.distances = np.zeros(10)
    self.localAge = np.zeros(10)

    self.levelHeightMass = np.zeros(10)
    self.levelHeightDistance = np.zeros(10)
    self.distanceBinsAge = np.zeros(10)
    self.localAge2 = np.zeros(10)

    self.longitudinalPar = np.zeros(6)
    self.chi2 = 0

    self.wPhotons = 0
    self.wElectrons = 0
    self.wHadrons = 0
    self.wMuons = 0
    self.numberEMfromPreshower = 0

    self.pad = np.zeros(6)
    
