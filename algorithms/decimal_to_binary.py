#!/usr/bin/env python2

def convertInteger(decimal):
  """Converts a real integer's representation from decimal to binary.

  args:
    decimal: integer decimal number.

  returns:
    binary integer as string.
  """
  binary = ''
  if decimal > 1:
    binary += convertInteger(decimal/2)
    binary += str(decimal % 2)
    return str(binary)
  else:
    return '1'

print convertInteger(55)
