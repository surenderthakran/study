#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""From a live stream of integers (created by generating random numbers), keep
track of the median of all the previous elements.

Median of a sorted array of elements is the value of the middle
element of the array if the array has odd number of elements.
If the array has even number of elements, the median is the mean(average) of
the values of the two middle elements.

Solution:
For our problem we don't necessarily need to keep our array sorted. We just
need to find a value which divides the array in two halves where we can readily
access the largest element of the first half and smallest element of the second
half.
We can employ min and max heaps for our solution.
The left half of the array will be represented by a max heap and the second
with a min heap.
When a new element is generated, we compare it with the existing median value.
If it is smaller than the existing median, we add it to the left half's max
heap. If it is greater we add it to the right half's min heap. (Adding element
to a heap also includes re-heapifing the heaps.)
After adding the new element to the heap, if the number of elements in either
heap is more than 1 greater than the number of elements in the other, we remove
the root element from the larger heap and add it to the other heap. This way at
any point no heap has more than 1 more element than the other heap.
If the two heaps have equal number of elements, the median would be the mean of
the roots of both the heaps.
If the two heaps don't have equal number of elements, the median would be the
root of the heap with more elements.

Usage:
$ python track_median.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

if __name__ == '__main__':
  pass
