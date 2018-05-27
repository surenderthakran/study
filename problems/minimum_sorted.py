#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Find the smallest integer element in a rotated sorted list.

The sorted rotated array, unlike a sorted array, will have one pair of
consecutive elements where the left is greater than the right.
We use a technique similar to the binary search to find the minimum element.

Usage:
$ python minimum_sorted.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def find_minimum_in_rotated_sorted_list(arr):
  """Returns the minimum element on the given rotated sorted list.

  Args:
    arr: a rotated sorted list.

  Returns:
    smallest integer element in the list.
  """
  low = 0
  high = len(arr) - 1

  # Will be false if the list is not rotated.
  while arr[high] < arr[low]:
    mid = low + (high - low)//2

    # If mid is the reset point.
    if arr[mid - 1] > arr[mid]:
      low = mid
    # If the first half has the reset point.
    elif arr[mid] < arr[low]:
      high = mid - 1
    # If the second half has the reset point.
    elif arr[high] < arr[mid]:
      low = mid + 1

  return arr[low]

if __name__ == '__main__':
  arr = [6, 7, 1, 2, 3, 4, 5]
  print(find_minimum_in_rotated_sorted_list(arr))
