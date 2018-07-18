#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implementing power function.

The power function operates with a time complexity of O(logn).

The solution operates on two power equations.
x ^ n = (x ^ a) * (x ^ b), if n = a + b
and
x ^ n = (x ^ a) ^ b, if n = a * b

Usage:
$ python power.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def power(base, exp):
  """Implements a basic power function.

  Args:
    base: (float) Base number to be raised.
    exp: (int) Exponent integer to raise the base.

  Returns:
    Float value of the base raised to the power of exp.
  """
  if exp == 0:
    return 1

  # If exponent is even, square the base and iteratively solve for base ^ exp/2.
  if exp % 2 == 0:
    result = base ** 2
    return power(result, exp / 2)

  # If exponent is odd, square the base and iteratively solve for
  # base ^ (exp-1)/2 while multiplying the result with the base once.
  result = base ** 2
  return base * power(result, (exp - 1) / 2)


if __name__ == '__main__':
  assert power(2, 0) == 1

  assert power(2, 1) == 2
  assert power(-2, 1) == -2

  assert power(2, 2) == 4
  assert power(-2, 2) == 4

  assert power(2, 3) == 8
  assert power(-2, 3) == -8

  assert power(4, 3) == 64
  assert power(-4, 3) == -64
