#!/usr/bin/env python2

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

def convertInteger(binary):
  """Converts a integer's representation from binary to decimal.

  args:
    binary: integer in binary as an int data type.

  returns:
    decimal representation of the integer.
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

print(convertInteger(110110))
