#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implementing selection sort.

Selecton sort operates in O(n^2) time complexity.

Selection sort works by repeating two steps for each array element:
1. Find the shortest element from elements to the right of the current element.
2. Swap the shortest element with the immediate right element.

In an array of length n, the above steps will be repeated n - 1 times since by
the time we reach the second last element, the last element would already be
in its proper position. Hence, the time complexity of this operation is O(n).

Finding the shortest element is performed through a linear search where the
elements we compare with  are reduced as we move along the array.
While processing the first element, we have to linear search in  n elements.
For second element we compare with n - 1 elements and so on.
Total number of comparisons for all n elements of the array are:
n + (n-1) + (n-2) + (n-3) + ..... + 2 = (n(n + 1)/ 2) - 1 = (n^2 + n)/2 - 1
= (n^2 + n - 2)/2
Since we only look at the highest order of the polynomial when deducing
complexities, the time complextiy for this step is O(n^2).

Swapping two numbers is a constant time operation so it does not factors while
computing time complexity.

Hence, the total time complexity is factor of O(n) and O(n^2).

Since complexity of an algorithm is that of the step with the highest order,
the time complexity is O(n^2).

Usage:
$ python selection_sort.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def shortest(arr, beg):
  shortest_index = beg
  for i in range(beg, len(arr)):
    if arr[i] < arr[shortest_index]:
      shortest_index = i

  return shortest_index


def selection_sort(arr):
  for writer_index in range(len(arr) - 1):
    shortest_index = shortest(arr, writer_index)
    arr[writer_index], arr[shortest_index] = (
        arr[shortest_index], arr[writer_index])


if __name__ == '__main__':
  array = [9, 7, 5, 3, 1, 8, 6, 4, 2]
  selection_sort(array)
  assert array == [1, 2, 3, 4, 5, 6, 7, 8, 9]
