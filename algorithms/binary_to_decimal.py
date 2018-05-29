#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Converts binary numbers (both integers and real) to decimals.

Usage:
$ python binary_to_decimal.py <binary_input>

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


def convert_integer(binary_integer):
  """Converts a integer's representation from binary to decimal.

  Decimal value of a binary integer is a sum of multiples of the digit
  and 2 raised to the power of position of the digit.

  ex: 1010 = (1 * 2 ** 3) + (0 * 2 ** 2) + (1 * 2 ** 1) + (0 * 2 ** 0)

  Args:
    binary_integer: integer in binary as an int data type.

  Returns:
    decimal representation of the integer.

  Raises:
    ValueError: for invalid binary numbers.

  """
  decimal = 0
  position = 0
  while binary_integer != 0:
    # get least significant digit
    num = binary_integer % 10
    if num > 1:
      raise ValueError('Invalid input binary number:', binary_integer)

    # calculate decimal value of the binary digit
    val = num * 2**position

    # add digit's decimal value to the total decimal value
    decimal += val

    # remove least significant bit by floor division
    binary_integer //= 10

    # increment position by 1
    position += 1

  return decimal


def convert_fraction(binary_fraction):
  """Converts a binary's fractional part to decimal.

  Decimal value of the binary fractio is a sun of multiple of the digit and
  2 raise to the power of negative position of the digit.

  ex: 0.1010 = (1 * 2 ** -1) + (0 * 2 ** -2) + (1 * 2 ** -3) + (0 * 2 ** -4)

  Args:
    binary_fraction: binary fractional number as string.

  Returns:
    decimal value of the binary fraction as integer.

  Raises:
    ValueError: if the binary fraction is invalid.
  """
  fraction = binary_fraction
  decimal = 0
  position = 1

  # iterate till fraction is not empty.
  while fraction:
    # get first digit from the left.
    digit = fraction[:1]

    # convert string character to int.
    num = int(digit)
    if num > 1:
      raise ValueError('Invalid binary fraction:', binary_fraction)

    # get decimal value of the digit.
    val = num * (1 / 2 ** position)

    # add decimal value of the digit to the tial decimal value.
    decimal += val

    # remove the first digit from the binary string.
    fraction = fraction[1:]

    # increment position by 1.
    position += 1

  return decimal

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise ValueError('No binary input found')

  arg = sys.argv[1]

  # Validate if input is a real number. It will always return a float as string.
  arg = str(float(arg))

  # split integer and fractional part from the number.
  binary_split = arg.split('.')

  # convert integer part to decimal.
  result = convert_integer(int(binary_split[0])) if binary_split[0] else 0

  # convert fractional part to decimal and add to the integer result.
  result += convert_fraction(binary_split[1]) if binary_split[1] else 0

  print('Decimal:', result)

