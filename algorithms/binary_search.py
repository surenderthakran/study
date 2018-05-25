#!/usr/bin/env python2
# -*- coding: utf-8  -*-

"""Find position of an element in a sorted array using binary search.

Usage:
$ python binary_search.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def binary_search(arr, elem):
  """Return index of the given element in the list.

  If the element doesn't exists in the list return -1.

  Args:
    arr: list of integers.
    elem: integer element to find in the array.

  Returns:
    integer position of the element or -1 if the element doesn't exists.
  """
  low = 0
  high = len(arr) - 1

  while high >= low:
    mid = low + (high - low)//2
    if elem == arr[mid]:
      return mid
    elif elem < arr[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return -1

if __name__ == '__main__':
  arr = [1, 3, 5, 7, 9, 11, 13, 15]
  print(binary_search(arr, 5))
