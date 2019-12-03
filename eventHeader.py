#===============================================
# eventHeader
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

try:
  from corsikaMessage import corsikaMessage
except ImportError:
  from .corsikaMessage import corsikaMessage

from math import log10
import numpy as np

class _seeds:
  def __init__(self, seed, iMod, iDiv):
    self.seed = seed
    self.initialCallMod = iMod
    self.initialCallDiv = iDiv


class eventHeader:
  def __init__(self, words):
    printer = corsikaMessage(1)
    printer.DEBUG( str(words) )
    self.ID				= blockID(words.pop(0))
    self.eventNumber			= words.pop(0)
    self.particleID			= words.pop(0)
    self.energy				= words.pop(0)
    self.startingAltitude		= words.pop(0)
    self.firstTarget			= words.pop(0)
    self.zFirst				= words.pop(0)
    self.px				= words.pop(0)
    self.py				= words.pop(0)
    self.pz				= words.pop(0)
    self.theta				= words.pop(0)
    self.phi				= words.pop(0)
    self.randomSequences		= words.pop(0)
    self.seeds                          = []

    for i in range(10):
      self.seeds.append( _seeds( words.pop(0), words.pop(0), words.pop(0) )) #10*3+13 = 43 last
    
    self.runNumber			= words.pop(0)
    self.dateStart			= words.pop(0)
    self.version			= words.pop(0)
    self.obsLevels			= int(words.pop(0))
    self.obsHeight			= [] # cm
    for i in range(self.obsLevels):
      self.obsHeight.append(words.pop(0))
    self.spectralSlope			= words.pop(0)
    self.eMin				= words.pop(0) # GeV
    self.eMax				= words.pop(0)
    self.cutoffHad			= words.pop(0)
    self.cutoffMu			= words.pop(0)
    self.cutoffEl			= words.pop(0)
    self.cutoffPh			= words.pop(0)
    self.constNFLAIN			= words.pop(0)
    self.constNFLDIF			= words.pop(0)
    self.constNFLPI0			= words.pop(0)
    self.constNFLPIF			= words.pop(0)
    self.constNFLPCHE			= words.pop(0)
    self.constNFRAGM			= words.pop(0)
    self.bx				= words.pop(0)
    self.by				= words.pop(0)
    self.flagEGS4			= words.pop(0)
    self.flagNKG			= words.pop(0)
    self.flagLowEnergyModel		= words.pop(0)
    self.flagHighEnergyModel		= words.pop(0)
    self.flagCherenkov			= words.pop(0)
    self.flagNeutrino			= words.pop(0)
    self.flagCurved			= words.pop(0)
    self.flagComputer			= words.pop(0)
    self.thetaMin			= words.pop(0)
    self.thetaMax			= words.pop(0)
    self.phiMin				= words.pop(0)
    self.phiMax				= words.pop(0)
    self.cherenkovBunch			= words.pop(0)
    self.cherenkovNumberX		= words.pop(0)
    self.cherenkovNumberY		= words.pop(0)
    self.cherenkovGridX			= words.pop(0)
    self.cherenkovGridY			= words.pop(0)
    self.cherenkovDetectorX		= words.pop(0)
    self.cherenkovDetectorY		= words.pop(0)
    self.cherenkovOutputFlag		= words.pop(0)
    self.arrayRotation			= words.pop(0)
    self.flagMuonAdditionalInformation	= words.pop(0)
    self.multipleScatteringStep		= words.pop(0)
    self.cherenkovBandwidthMin		= words.pop(0)
    self.cherenkovBandwidthMax		= words.pop(0)
    self.usesOfCherenkovEvent		= words.pop(0)
    self.coreX				= []
    
    for i in range(20):
      self.coreX.append( words.pop(0) )
    self.coreY				= []
    for i in range(20):
      self.coreY.append( words.pop(0) )
    self.flagSybill			= words.pop(0)
    self.flagSybillCross		= words.pop(0)
    self.flagQGSJet			= words.pop(0)
    self.flagQGSJetCross		= words.pop(0)
    self.flagDPMJet			= words.pop(0)
    self.flagDPMJetCross		= words.pop(0)
    self.flagVenusCross			= words.pop(0)
    self.flagMuonMultiple		= words.pop(0)
    self.NKGRadialRange			= words.pop(0)
    self.eFractionThinningH		= words.pop(0)
    self.eFractionThinningEM		= words.pop(0)
    self.wMaxHadronic			= words.pop(0)
    self.wMaxEm				= words.pop(0)
    self.innerAngle			= words.pop(0)
    self.outerAngle			= words.pop(0)
    self.highLowEnergyTransition	= words.pop(0)
    self.skimmingIncidence		= words.pop(0)
    self.skimmingAxisAltitude		= words.pop(0)
    self.startingHeight			= words.pop(0)
    self.flagCharm			= words.pop(0)
    self.flagEmAdditionalInformation	= words.pop(0)
    self.unused				= []
    for i in range(7):
      self.unused.append( words.pop(0) )
    self.curvedObsLevel			= words.pop(0)
    printer.DEBUG( str(self.theta) )
    printer.DEBUG( str(self.version) )


  def __str__(self):
    s  = "event number: "
    s += str(self.eventNumber)
    s += "\t| energy: "
    s += str(log10( self.energy )+9)
    s += " eV\t|"
    return s



  
