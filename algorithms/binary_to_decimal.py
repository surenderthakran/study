# -*- coding: utf-8 -*-
#!/usr/bin/env python2

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

class InvalidInputException(Exception):
  """Custom exception class for invalid inputs to the program."""

def convertInteger(binary_input):
  """Converts a integer's representation from binary to decimal.

  args:
    binary_input: integer in binary as an int data type.

  returns:
    decimal representation of the integer.
  """
  decimal = 0
  position = 0
  while binary_input != 0:
    # get least significant digit
    num = binary_input % 10

    if num > 1:
      raise ValueError('Invalid input binary number:', binary_input)

    # calculate decimal value of the binary digit
    val = num * 2**position
    decimal += val

    # remove least significant bit by floor division
    binary_input = binary_input//10

    # increment position by 1
    position += 1

  return decimal

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise InvalidInputException('No binary input found')

  try:
    binary = int(sys.argv[1])
  except ValueError:
    raise InvalidInputException('Invalid binary input:', sys.argv[1])

  print(convertInteger(int(sys.argv[1])))
