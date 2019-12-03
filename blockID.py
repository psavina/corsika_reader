#===============================================
# blockID
#===============================================
#
#
#===============================================

import struct

class blockID:
  def __init__(self, head):
    self.lenght = 4
    self.ID = head

  def isA(self, head ):

    return self.ID == head
