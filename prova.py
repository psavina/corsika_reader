#!/usr/bin/python

from math import log10
from rawCorsikaFile import rawCorsikaFile
f = rawCorsikaFile('/storage/gpfs_data/auger/psavina/Simulations/EPOS_LHC/protons/185_190/DAT448059.part')
f.next(0)
print(log10(f.diskBlock.subBlocks[1].data.energy)+9)
f.close()
