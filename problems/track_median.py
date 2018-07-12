#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Keep track of the median in a live stream of integers.

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

from abc import ABCMeta
from abc import abstractmethod


class Heap(object):
  __metaclass__ = ABCMeta

  def __init__(self, arr=None):
    if not arr:
      self.arr = []
      return

    self.arr = arr
    self.heapify()

  def left_index(self, index):
    left_index = 2 * index + 1
    if left_index > len(self.arr) - 1:
      return -1

    return left_index

  def left(self, index):
    left_index = self.left_index(index)
    if left_index == -1:
      return None

    return self.arr[left_index]

  def right_index(self, index):
    right_index = 2 * index + 2
    if right_index > len(self.arr) - 1:
      return -1

    return right_index

  def right(self, index):
    right_index = self.right_index(index)
    if right_index == -1:
      return None

    return self.arr[right_index]

  def parent_index(self, index):
    parent_index = (index - 1) // 2
    if parent_index < 0:
      return -1

    return parent_index

  def parent(self, index):
    parent_index = self.parent_index(index)
    if parent_index == -1:
      return None

    return self.arr[parent_index]

  def heap_array(self):
    return self.arr

  def add(self, element):
    self.arr.append(element)

    self.bubble_up(len(self.arr) - 1)

  @abstractmethod
  def bubble_up(self, index):
    pass

  def remove(self):
    if not self.arr:
      return None

    root = self.arr[0]

    self.arr[0] = self.arr[-1]

    self.arr = self.arr[:-1]

    self.sink_down(0)

    return root

  @abstractmethod
  def sink_down(self, index):
    pass

  def heapify(self):
    if len(self.arr) < 2:
      return

    last_parent = self.parent_index(len(self.arr) - 1)

    for parent_index in range(last_parent, -1, -1):
      self.sink_down(parent_index)

  def delete(self, index):
    if index > len(self.arr) - 1:
      return

    self.arr[index] = self.arr[-1]
    self.arr = self.arr[:-1]

    self.sink_down(index)


class MinHeap(Heap):

  def __init__(self, arr=None):
    Heap.__init__(self, arr)

  def bubble_up(self, index):
    parent = self.parent(index)
    if parent and self.arr[index] < parent:
      tmp = parent
      self.arr[self.parent_index(index)] = self.arr[index]
      self.arr[index] = tmp

      self.bubble_up(self.parent_index(index))

  def sink_down(self, index):
    smallest = index

    left = self.left(index)
    if left and left < self.arr[smallest]:
      smallest = self.left_index(index)

    right = self.right(index)
    if right and right < self.arr[smallest]:
      smallest = self.right_index(index)

    if smallest == index:
      return

    tmp = self.arr[index]
    self.arr[index] = self.arr[smallest]
    self.arr[smallest] = tmp

    self.sink_down(smallest)


def test_min_heap():
  min_heap = MinHeap([35, 33, 42, 10, 14, 19, 27, 44, 26, 31])

  assert min_heap.heap_array() == [10, 14, 19, 26, 31, 42, 27, 44, 33, 35]

  assert min_heap.remove() == 10

  assert min_heap.heap_array() == [14, 26, 19, 33, 31, 42, 27, 44, 35]

  # Deleting out of bounds index.
  min_heap.delete(9)

  assert min_heap.heap_array() == [14, 26, 19, 33, 31, 42, 27, 44, 35]

  # Deleting last index.
  min_heap.delete(8)

  assert min_heap.heap_array() == [14, 26, 19, 33, 31, 42, 27, 44]

  min_heap.delete(2)

  assert min_heap.heap_array() == [14, 26, 27, 33, 31, 42, 44]

  min_heap.add(15)

  assert min_heap.heap_array() == [14, 15, 27, 26, 31, 42, 44, 33]


if __name__ == '__main__':
  test_min_heap()
