#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


def convertIntegerWithRecursion(decimal):
  """Converts a real integer's representation from decimal to binary.

  args:
    decimal: integer decimal number.

  returns:
    binary integer as string.
  """
  binary = ''
  if decimal > 1:
    binary += convertIntegerWithRecursion(decimal//2)
    binary += str(decimal % 2)
    return str(binary)
  else:
    return '1'


def convertIntegerWithLoops(decimal):
  result = ''
  # iterate until the remaining value is less than the base, 2.
  while decimal > 1:
    val = decimal % 2
    result += str(val)

    decimal = decimal // 2

  result += str(decimal)

  # reverse the result string by swapping numbers from both ends.
  arr = list(result)
  start = 0
  end = len(arr) - 1
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

  return ''.join(arr)

def convertFraction():

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise ValueError('No decimal argument found')

  arg = str(float(sys.argv[1]))

  arg_split = arg.split('.')

  result1 = convertIntegerWithLoops(arg_split[0]) if arg_split[0] else '0'
  result1 += (
      result1 + '.' + convertFraction(int(arg_split[1]))
          if arg_split[1] else '0')

  print(result1)

  result2 = convertIntegerWithRecursion(arg_split[0]) if arg_split[0] else '0'
  result2 += (
      result2 + '.' + convertFraction(int(arg_split[1]))
          if arg_split[1] else '0')
  print(result2)
