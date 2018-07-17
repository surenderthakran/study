#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implementing quick sort.

The quick sort algorithm operates in O(n logn) time complexity in best & average
case and O(n^2) is worst case.

Quick Sort is a divide and conquer algorithm hence it is divided in three steps:
1. Divide
   During the divide part we choose a pivot element (usually the last element)
   in the given array and put it in its proper position in the array. i.e. all
   the elements smaller than the pivot element are to its left and all larger
   elements are to its right.
   Since we iterate through all elements in the given array, positioning the
   pivot to its proper position happens in O(n) time.
   After positioning the pivot we split our array in two sub-arrays. This
   happens in constant time O(1).
2. Conquer
   This is the part where we recursively sort the sub-arrays. In average and
   best case, the arrays would be split logn times.
   For worst case (where the input array is sorted in reverse), the arrays
   will be split n times.
3. Combine
   No action is needed here since quick sorts works completely in-place.

Usage:
$ python quicksort.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def quick_sort(arr, beg=None, end=None):
  """Sorts the mentioned array segment.

  Args:
    arr: (list) List of integers.
    beg: (int) Starting index of the array portion to be sorted.
    end: (int) Ending index of the array portion to be sorted.
  """
  # If beginning and ending index are unknown, assume that the whole array has
  # to be sorted.
  if beg is None and end is None:
    beg = 0
    end = len(arr) - 1

  # Only sort if beginning index is less than the ending index.
  if beg < end:
    # We choose the last element in the sub-array as our pivot element.
    pivot_index = end

    # We place our reader and writer indices at the beginning of the sub-array.
    reader_index = beg
    writer_index = beg

    # Iterate until we have reached the pivot element at the end of the
    # sub-array.
    while reader_index <= pivot_index:
      # If the element at the reader's index is smaller than the pivot.
      if arr[reader_index] <= arr[pivot_index]:
        # Swap reader's and writer's elements.
        arr[reader_index], arr[writer_index] = (
            arr[writer_index], arr[reader_index])
        # Increment writer's index by 1.
        writer_index += 1

      # Always increment reader's index by 1.
      reader_index += 1

    # Recursively sort the sub-arrays to the left and right of the pivot's new
    # position.
    quick_sort(arr, beg, writer_index - 2)
    quick_sort(arr, writer_index, end)


if __name__ == '__main__':
  array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
  quick_sort(array)
  assert array == [1, 2, 3, 4, 5, 6, 7, 8, 9]
