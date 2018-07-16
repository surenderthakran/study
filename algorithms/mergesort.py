#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implementing merge sort.

Usage:
$ python mergesort.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def merge(arr1, arr2):
  """Merges two sorted arrays to return one single sorted array.

  Args:
    arr1: (list) Sorted list of integers.
    arr2: (list) Sorted list of integers.

  Returns:
    Sorted list of integers.
  """
  i = 0
  j = 0
  result = []

  # Merge two arrays by picking the smallest element from the head of the two
  # arrays and writing it in the new array.
  # Loop until atleast one array has been completely consumed.
  while i <= len(arr1) - 1 and j <= len(arr2) - 1:
    # If element at arr1's head is smaller than the element at arr2's head,
    # write arr1's head to the new array.
    if arr1[i] < arr2[j]:
      result.append(arr1[i])
      i += 1
    else:
      # Else write arr2's head to the new array.
      result.append(arr2[j])
      j += 1

  # Copy all the remaining element from arr1 or arr2 to the new array.
  if i <= len(arr1) - 1:
    result += arr1[i:]
  else:
    result += arr2[j:]

  return result


def merge_sort(arr):
  """Recursively sorts the given array.

  Args:
    arr: (list) List of integers.

  Returns:
    Sorted list of integers.
  """
  # Return list of its length is 1.
  if len(arr) == 1:
    return arr
  else:
    l = 0
    r = len(arr) - 1

    # Calculate middle point in the array.
    m = (l + r) // 2

    # Recursively sort the left part of the array.
    left = merge_sort(arr[l:m+1])

    # Recursively sort the right part of the array.
    right = merge_sort(arr[m+1:r+1])

    # Merge and return the sorted array.
    return merge(left, right)


if __name__ == '__main__':
  assert merge_sort([9, 1, 8, 2, 7, 3, 6, 4, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
