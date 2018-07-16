#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def merge(arr1, arr2):
  i = 0
  j = 0
  result = []
  while i <= len(arr1) - 1 and j <= len(arr2) - 1:
    if arr1[i] < arr2[j]:
      result.append(arr1[i])
      i += 1
    else:
      result.append(arr2[j])
      j += 1

  if i <= len(arr1) - 1:
    result += arr1[i:]

  if j <= len(arr2) - 1:
    result += arr2[j:]

  return result


def merge_sort(arr):
  if len(arr) == 1:
    return arr
  else:
    l = 0
    r = len(arr) - 1

    m = (l + r) // 2

    left = merge_sort(arr[l:m+1])

    right = merge_sort(arr[m+1:r+1])

    return merge(left, right)


if __name__ == '__main__':
  assert merge_sort([9, 1, 8, 2, 7, 3, 6, 4, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
