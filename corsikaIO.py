#=======================================================================
# corsikaIO
#-----------------------------------------------------------------------
# author Pierpaolo Savina
# date   27/11/2019
#
#=======================================================================

# struct used to convert 
import struct

try:
  from corsikaMessage import corsikaMessage
except ImportError:
  from .corsikaMessage import corsikaMessage


class corsikaIO:
  def __init__(self, filename, verbose = 0):

    self.corsikaFile = open( filename, 'rb' )
    
