#=======================================================================
# corsikaMessage
#-----------------------------------------------------------------------
# author Pierpaolo Savina
# date   27/11/2019
#
#=======================================================================
class corsikaMessage:
  def __init__(self, verbosity):
    self.v = verbosity

  def INFO(self, m):
    message  = "["
    message += "\033[1m"
    message += "INFO "
    message += "\033[0m"
    message += "] "
    message += m

    if self.v >= 2:
      print(message)
  
  def DEBUG(self, m):
    message  = "["
    message += "\033[1m"
    message += "\033[32m"
    message += "DEBUG"
    message += "\033[0m"
    message += "] "
    message += m

    if self.v >= 3:
      print(message)

  def WARN(self, m):
    message  = "["
    message += "\033[1m"
    message += "\033[33m"
    message += "WARN "
    message += "\033[0m"
    message += "] "
    message += m

    if self.v >= 1:
      print(message)

  def ERROR(self, m):
    message  = "["
    message += "\033[1m"
    message += "\033[31m"
    message += "ERROR"
    message += "\033[0m"
    message += "] "
    message += m

    if self.v >= 0:
      print(message)
