try:
  from corsikaMessage import corsikaMessage
except ImportError:
  from .corsikaMessage import corsikaMessage

try:
  from rawCorsikaFile import rawCorsikaFile
except ImportError:
  from .rawCorsikaFile import rawCorsikaFile
