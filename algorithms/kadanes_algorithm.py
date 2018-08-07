#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implement Kadane's algorithm.

Use Kadane's algorithm to find out the largest sum of consecutive elements in
an array.

ex: In the array, [-5, 6, 7, 1, 4, -8, 16] the largest sum of consecutive
elements is 26 for the sub-array [6, 7, 1, 4, -8, 16].

Kadane's algorithm works by deducing sum of smaller sub-arrays and comparing
it with the global highest sum.

1. Set both the current highest and the global highest equal to the value of
   the first element in the array.
2. Start iterating over each element.
3. For every new element, determine the current highest sum. The new current
   highest sum is greater of the existing current highest plus the new element
   or the new element alone.
4. Compare every new current highest sum with the global highest sum and
   replace it if it is greater.
5. The final global highest sum at the end of the iteration should be the
   solution.

It operates in O(n) time complexity since there is only a single iteration over
the input array. Everything else is in constant time.

Usage:
$ python kadanes_algorithm.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def kadane(arr):
  """Returns the largest sum of consecutive elements in the array."""
  length = len(arr)
  # set global and current highest to first element's value.
  global_highest = arr[0]
  current_highest = arr[0]

  for i in range(length):
    # deduce current highest with every new element encountered.
    current_highest = max(current_highest + arr[i], arr[i])

    # replace global highest if current highest is greater.
    if current_highest > global_highest:
      global_highest = current_highest

  return global_highest


if __name__ == '__main__':
  assert kadane([-5, 6, 7, 1, 4, -8, 16]) == 26
  assert kadane([-1, 2, 2, -1, -1, -1, -1, -1, 3, 4, 5, -1]) == 12
