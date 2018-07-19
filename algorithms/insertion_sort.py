#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implementing insertion sort.

Insertion sort operates this O(n^2) time complexity on worst case.

Insertion sort can be divided in two repeatitive steps.
1. Iterating over each element in the array to place it in its proper position.
2. Moving elements to the right while placing the element to its position.

Step one will be performed for every element in the array, hence its time
complexity is O(n).

Worst case for insertion sort in where the array is already sorted in reverse.
For worst case, in step two, the number of elements to be moved will increase
every time we read a new element.
When reading the first element, 0 elements would have to be moved. For the
second element, 1 element will me moved and so on.
Total number of elements moved in worst case for an array of length n is:
0 + 1 + 2 + 3 + .... + (n-1) = n(n - 1)/2 = (n^2 - n)/2
Since it is a second order polynomial equation, the time complexity is O(n^2).

Since we only consider the highest order when calculating complexities, the
time complexity in worst case is O(n^2).

Best case for insertion sort is where the array is already sorted.
In best case, in step two, no movement will ever be needed. So step two can be
disregarded.

Hence, best case time complexity for insertion sort is O(n).

Usage:
$ python insertion_sort.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def insertion_sort(arr):
  """Sorts an integer array using insertion sort."""
  # Read every element in the array to put it in its proper position in the
  # sorted array on the left.
  for reader_index in range(len(arr)):
    reader_value = arr[reader_index]

    # Loop in reverse in the sorted array on the left.
    i = reader_index - 1
    while i >= 0 and arr[i] >= reader_value:
      # Move all elements greater than the read element one place to the right.
      arr[i + 1] = arr[i]
      i -= 1

    # Place the read element at the position of the last element larger than it
    # or at the beginning of the array if all elements were larger than it.
    arr[i + 1] = reader_value


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
    insertion_sort(test_case['input'])
    assert test_case['input'] == test_case['output']
