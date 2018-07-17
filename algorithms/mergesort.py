#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implementing merge sort.

Usage:
$ python mergesort.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def merge(arr, l, m, r):
  """Merges two sorted portions of a list subset to form a single subset.

  Args:
    arr: (list) List of integers.
    l: (int) Starting index of the list's sorted left portion.
    m: (int) Index separating the left and right sorted portions of the list.
    r: (int) Ending index of the list's sorted right portion.
  """
  i = l
  j = m + 1
  result = []

  # Merge two sorted portions by picking the smallest element from the head of
  # the two portions and writing it in the new array.
  # Loop until atleast one portion has been completely consumed.
  while i <= m and j <= r:
    # If element at left portion's current head is smaller than the element at
    # right portion's current head, write left portion's head to the new array.
    if arr[i] < arr[j]:
      result.append(arr[i])
      i += 1
    else:
      # Else write right portion's head to the new array.
      result.append(arr[j])
      j += 1

  # Copy all the remaining element from left or right portion to the new array.
  if i <= m:
    result += arr[i:m+1]
  else:
    result += arr[j:r+1]

  # Write the new sorted array's elements over the element of the left and
  # right portions.
  for index, value in enumerate(result):
    arr[l + index] = value


def merge_sort(arr, l=None, r=None):
  """Recursively merge sorts the given array in-place.

  Args:
    arr: (list) List of integers.
    l: (int) Starting index of the array subset to sort.
    r: (int) Ending index if the array subset to sort.
  """
  # If l and r are None, it means we need to sort the whole array.
  if l is None and r is None:
    l = 0
    r = len(arr) - 1

  # Sort only if l is smaller than r. Don's sort if l == r since we cannot sort
  # a single element.
  if l < r:
    # Calculate mid point of the array subset.
    m = (l + r) // 2

    # Recursively sort the left portion of the array subset,
    merge_sort(arr, l, m)

    # recursively sort the right portion of the array subset.
    merge_sort(arr, m+1, r)

    # Merge the left and right portions to form a single sorted array subset.
    merge(arr, l, m, r)


if __name__ == '__main__':
  array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
  merge_sort(array)
  assert array == [1, 2, 3, 4, 5, 6, 7, 8, 9]
