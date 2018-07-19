#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implementing merge sort.

Merge sorts implements in O(n logn) time complexity in all three cases.

For an input array of size n, if we keep splitting it in half until we get
sub-arrays of size 1, we will be splitting logn times.
At each split level we merge/combine back ALL the subarrays, so the combined
merging time at each level is O(n).
Hence the totla time complexity of merge sort is O(n logn).

Usage:
$ python mergesort.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def merge(arr, l, m, r):
  """Merges two sorted portions of a list subset to form a single subset.

  Merging of two arrays with the below method takes O(n) time and O(n) space.

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

  Splitting an array in half takes constant time O(1).
  But the number of splits needed until we reach sub-array size 1 is n*logn.

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
  test_cases = [
      {
          'input': [],
          'output': [],
      },
      {
          'input': [2],
          'output': [2],
      },
      {
          'input': [2, 2],
          'output': [2, 2],
      },
      {
          'input': [1, 2, 3, 4, 5, 6, 7, 8, 9],
          'output': [1, 2, 3, 4, 5, 6, 7, 8, 9],
      },
      {
          'input': [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9],
          'output': [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9],
      },
      {
          'input': [9, 8, 7, 6, 5, 4, 3, 2, 1],
          'output': [1, 2, 3, 4, 5, 6, 7, 8, 9],
      },
      {
          'input': [9, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1],
          'output': [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9],
      },
      {
          'input': [-1, -2, -3, -4, -5, -6, -7, -8, -9],
          'output': [-9, -8, -7, -6, -5, -4, -3, -2, -1],
      },
      {
          'input': [-1, -2, -3, -3, -4, -5, -6, -7, -8, -9],
          'output': [-9, -8, -7, -6, -5, -4, -3, -3, -2, -1],
      },
      {
          'input': [9, 7, 5, 3, 1, 2, 4, 6, 8],
          'output': [1, 2, 3, 4, 5, 6, 7, 8, 9],
      },
      {
          'input': [1, 9, 2, 8, 3, 7, 4, 6, 5],
          'output': [1, 2, 3, 4, 5, 6, 7, 8, 9],
      },
      {
          'input': [1, 9, 2, -8, 3, 7, -4, 6, -5],
          'output': [-8, -5, -4, 1, 2, 3, 6, 7, 9],
      },
  ]

  for test_case in test_cases:
    print(test_case)
    merge_sort(test_case['input'])
    assert test_case['input'] == test_case['output']
