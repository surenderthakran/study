#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def quick_sort(arr, beg=None, end=None):
  if beg is None and end is None:
    beg = 0
    end = len(arr) - 1

  if beg < end:
    pivot_index = end

    reader_index = beg
    writer_index = beg

    while reader_index <= pivot_index:
      if arr[reader_index] <= arr[pivot_index]:
        arr[reader_index], arr[writer_index] = arr[writer_index], arr[reader_index]
        writer_index += 1
      reader_index += 1

    quick_sort(arr, beg, writer_index - 2)
    quick_sort(arr, writer_index, end)


if __name__ == '__main__':
  array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
  quick_sort(array)
  assert array == [1, 2, 3, 4, 5, 6, 7, 8, 9]
