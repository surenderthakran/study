#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Converts decimal numbers (both integer and real) to binary.

Usage:
$ python decimal_to_binary.py <decimal_input>
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


def convert_integer_with_recursion(decimal):
  """Converts an integer's representation from decimal to binary.

  It uses the division method to convert using recursive calls to itself.

  Args:
    decimal: integer decimal number.

  Returns:
    binary integer as string.
  """
  binary = ''

  # convert any value greater than 1 to binary.
  if decimal > 1:

    # call the current function recursively with the floor division result.
    binary += convert_integer_with_recursion(decimal // 2)

    # add denominator of the decimal divided by 2 to the result.
    # this step comes after the recursive call because while converting
    # decimal to binary with division method the results are read backwards.
    binary += str(decimal % 2)

    return str(binary)
  else:
    # this could never be '0' since this will become the most significant bit
    # which can never be zero.
    return '1'


def convert_integer_with_loops(decimal):
  """Converts a decimal integer to binary.

  It uses the division method to convert using while loops.

  Args:
    decimal: integer decimal number

  Returns:
    binary integer as string
  """
  result = ''

  # iterate until the remaining value is less than the base, 2.
  while decimal > 1:

    # the binary value is the denominator of decimal divided by 2.
    val = decimal % 2

    # append the value to the result string.
    result += str(val)

    # update the decimal value to the floor division value for next iteration.
    decimal //= 2

  # when the decimal becomes less than 2, append it to the result string.
  result += str(decimal)

  # since in the division method the denominators are read in the reverse order
  # of their generation.
  # reverse the result string by swapping numbers from both ends.

  # convert the result string to list for reversal.
  arr = list(result)
  start = 0
  end = len(arr) - 1

  # iterate until the end value becomes smaller or equal to the start value.
  while start < end:
    # swap start and end values in the list.
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

  # convert the list back to string.
  return ''.join(arr)


def convert_fraction(fraction):
  """Converts the fractional part of a decimal number to binary.

  We convert a decimal fraction to binary by iteratively multiplying it by 2
  and appending the integer part to the result after taking it out of the
  multiplication result.
  The iteration continues until the decimal becomes 1.0 or until we have
  iterated for a sufficient number of times since not all numbers will lead
  to 1.0 after continuous multiplication.

  Args:
    fraction: a float decimal number.

  Returns:
    fractional part of the decimal as string.
  """
  result = ''
  iteration = 0
  while fraction != 1.0 and iteration < 5:
    fraction *= 2
    result += str(int(fraction))
    fraction -= int(fraction)
    iteration += 1

  return result

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise ValueError('No decimal argument found')

  # validate if the argument is a valid number by converting it to float.
  # it will always update the arg to a float string.
  arg = str(float(sys.argv[1]))

  # split integer and fractional parts.
  arg_split = arg.split('.')

  # convert decimal to binary using loops.
  result1 = convert_integer_with_loops(
      int(arg_split[0])) if arg_split[0] else '0'
  if arg_split[1]:
    result1 += '.' + convert_fraction(float('0.' + arg_split[1]))
  print(result1)

  # convert decimal to binary using recursion.
  result2 = convert_integer_with_recursion(
      int(arg_split[0])) if arg_split[0] else '0'
  if arg_split[1]:
    result2 += '.' + convert_fraction(float('0.' + arg_split[1]))
  print(result2)

