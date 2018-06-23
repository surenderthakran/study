#!/usr/bin/env python2
# -*- coding: utf-8  -*-

"""Find position of an element in a sorted array using binary search.

Usage:
$ python binary_search.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def binary_search_loop(arr, elem):
  """Return index of the given element in the list.

  It uses loops to perfrom the search.

  Args:
    arr: list of integers.
    elem: integer element to search in the list.

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

def binary_search_recursion(arr, ele):
  """Returns index of the given element in the list.

  It uses recursion to perfrom the search.

  Args:
    arr: list of integers.
    ele: integer element to search in the list.

  Returns:
    integer index of the element or -1 if the element doesn't exists.
  """
  if not arr:
    return -1

  mid = len(arr) // 2

  if arr[mid] == ele:
    return mid
  elif ele < arr[mid]:
    return binary_search_recursion(arr[:mid], ele)
  else:
    result = binary_search_recursion(arr[mid + 1:], ele)
    if result == -1:
      return -1
    return mid + 1 + result

if __name__ == '__main__':
  arr = [1, 3, 5, 7, 9, 11, 13, 15]
  assert binary_search_loop(arr, 5) == 2
  assert binary_search_recursion(arr, 5) == 2

  assert binary_search_loop(arr, 14) == -1
  assert binary_search_recursion(arr, 14) == -1

  assert binary_search_loop(arr, 0) == -1
  assert binary_search_recursion(arr, 0) == -1

  assert binary_search_loop(arr, 16) == -1
  assert binary_search_recursion(arr, 16) == -1
