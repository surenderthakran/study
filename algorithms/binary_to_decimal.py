#!/usr/bin/env python2

def convertInteger(binary):
  """Converts a real integer number's representation from binary to decimal.

  args:
    binary: integer binary number as int data type.

  returns:
    integer representation of the binary.
  """
  decimal = 0
  position = 0
  while binary != 0:
    num = binary % 10
    val = num * 2**position
    decimal += val
    binary = binary/10
    position += 1
  return decimal

print convertInteger(110110)
