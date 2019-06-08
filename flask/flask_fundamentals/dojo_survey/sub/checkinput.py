# from flask import request
# class CheckInput:
#   def __init__(self):
#     self.value = None
  
#   def checkForEmpty(self, val):
#     if len(val) != 0:
#       self.value  = val
#       return self.value
#     else:
#       self.val = ''
#       return self.value

def checkForEmpty(val=''):
  if (val):
    value  = val
    return value
  else:
    value = False
    return value