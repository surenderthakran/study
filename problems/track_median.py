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
  """Abstract class to implement heaps."""
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
    """Adds new element to the heap."""
    # Add element to the end of the heap.
    self.arr.append(element)

    # Bubble up the element to its proper position.
    self.bubble_up(len(self.arr) - 1)

  @abstractmethod
  def bubble_up(self, index):
    pass

  def remove(self):
    """Removes and returns the root element in the heap."""
    # Return None if the heap is empty.
    if not self.arr:
      return None

    # Set aside root element in the heap.
    root = self.arr[0]

    # replace root element with the last element.
    self.arr[0] = self.arr[-1]

    # Remove last element from the heap.
    self.arr = self.arr[:-1]

    # Sink down the new element at the root to its proper position.
    self.sink_down(0)

    return root

  def root(self):
    if not self.arr:
      return None

    return self.arr[0]

  def length(self):
    return len(self.arr)

  @abstractmethod
  def sink_down(self, index):
    pass

  def heapify(self):
    """Heapifies the complete binary tree represented by a list."""
    # If the tree has 0 or 1 element, there is no need to heapify it.
    if len(self.arr) < 2:
      return

    # We start from the last parent of the tree.
    # Last parent of the tree is the parent of the last element.
    last_parent = self.parent_index(len(self.arr) - 1)

    # Iterate from the last parent's position to the root.
    for parent_index in range(last_parent, -1, -1):
      # Sink down every element encountered to its proper position.
      self.sink_down(parent_index)

  def delete(self, index):
    """Deletes the element at the given index from the heap."""
    # Return if the index is out of bounds.
    if index > len(self.arr) - 1:
      return

    # Replace element at the given index with the last element.
    self.arr[index] = self.arr[-1]

    # Remove last element from the heap.
    self.arr = self.arr[:-1]

    # Sink down the new element at the index to its proper position.
    self.sink_down(index)


class MinHeap(Heap):
  """Class to implement a Min Heap."""

  def __init__(self, arr=None):
    Heap.__init__(self, arr)

  def bubble_up(self, index):
    """Bubble up the element at the given index to its proper position."""
    # Decude parent of the element at the given index.
    parent = self.parent(index)

    # If parent is larger than the element.
    if parent and self.arr[index] < parent:
      # Swap element with its parent.
      tmp = parent
      self.arr[self.parent_index(index)] = self.arr[index]
      self.arr[index] = tmp

      # Bubble up the element now at its parent's position.
      self.bubble_up(self.parent_index(index))

  def sink_down(self, index):
    """Sinks down the element at the given index to its proper position."""
    # Begin by assuming the index holds the smallest element amongst its
    # children.
    smallest = index

    # If left child exists and is smaller than the current smallest, make it
    # the new smallest.
    left = self.left(index)
    if left and left < self.arr[smallest]:
      smallest = self.left_index(index)

    # If right child exists and is smaller than the current smallest, amke it
    # the new smallest.
    right = self.right(index)
    if right and right < self.arr[smallest]:
      smallest = self.right_index(index)

    # Return if index still holds the smallest element.
    if smallest == index:
      return

    # Swap element at index with the smallest element.
    tmp = self.arr[index]
    self.arr[index] = self.arr[smallest]
    self.arr[smallest] = tmp

    # Sink down the element from its new position.
    self.sink_down(smallest)


class MaxHeap(Heap):
  """Class to implement Max Heap."""

  def __init__(self, arr=None):
    Heap.__init__(self, arr)

  def bubble_up(self, index):
    """Bubble up the element at the given index to its proper position."""
    # While the index has a parent and is larger than its parent.
    while self.parent(index) and self.arr[index] > self.parent(index):
      # Swap element with its parent.
      tmp = self.parent(index)
      self.arr[self.parent_index(index)] = self.arr[index]
      self.arr[index] = tmp

      # Set the element now at its parent's position for bubble up.
      index = self.parent_index(index)

  def sink_down(self, index):
    """Sinks down the element at the given index to its proper position."""
    # Let us start by assuming that the current index holds the largest element
    # amongst its children.
    largest = index

    # If the current index has a left child which is larger than the element at
    # the current index, then its index becomes the largest.
    left = self.left(index)
    if left and left > self.arr[largest]:
      largest = self.left_index(index)

    # If the current index has a right child which is larger than the current
    # index's element, then its index becomes that largest.
    right = self.right(index)
    if right and right > self.arr[largest]:
      largest = self.right_index(index)

    # Return if index still holds the largest element.
    if largest == index:
      return

    # Swap element at the index with the largest element.
    tmp = self.arr[largest]
    self.arr[largest] = self.arr[index]
    self.arr[index] = tmp

    # Sink down the element now at the new position.
    self.sink_down(largest)


def test_min_heap():
  """Function to check Min Heap implementation."""
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


def test_max_heap():
  """Function to check Max Heap implementation."""
  max_heap = MaxHeap([35, 33, 42, 10, 14, 19, 27, 44, 26, 31])

  assert max_heap.heap_array() == [44, 35, 42, 33, 31, 19, 27, 10, 26, 14]

  assert max_heap.remove() == 44

  assert max_heap.heap_array() == [42, 35, 27, 33, 31, 19, 14, 10, 26]

  max_heap.delete(9)

  assert max_heap.heap_array() == [42, 35, 27, 33, 31, 19, 14, 10, 26]

  max_heap.delete(2)

  assert max_heap.heap_array() == [42, 35, 26, 33, 31, 19, 14, 10]

  max_heap.delete(7)

  assert max_heap.heap_array() == [42, 35, 26, 33, 31, 19, 14]

  max_heap.add(40)

  assert max_heap.heap_array() == [42, 40, 26, 35, 31, 19, 14, 33]


def get_median(left_heap, right_heap):
  if left_heap.length() == right_heap.length():
    return (left_heap.root() + right_heap.root()) / 2

  if left_heap.length() > right_heap.length():
    return left_heap.root()

  return right_heap.root()


def track_median(element, left_heap, right_heap, median):
  """Returns new median for every new integer element."""
  # If no median already exists.
  if not median:
    # Add new element to the left heap.
    left_heap.add(element)
    # Calculate and return median.
    return get_median(left_heap, right_heap)

  if element < median:
    # Add element to the left heap if it is smaller than the existing median.
    left_heap.add(element)
  else:
    # Add element to the right heap if it is larger than the existing median.
    right_heap.add(element)

  # Transfer element between left and right heaps till no heap as more than one
  # element than the other element.
  while abs(left_heap.length() - right_heap.length()) > 1:
    if left_heap.length() > right_heap.length():
      # If left heap has more elements, remove one from left and add to right.
      tmp = left_heap.remove()
      right_heap.add(tmp)
    else:
      # If right heap has more elements, remove one from right and add to left.
      tmp = right_heap.remove()
      left_heap.add(tmp)

  # Calculate and return median.
  return get_median(left_heap, right_heap)


def test_track_median():
  """Function to test median tracking logic."""
  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

  # Left heap is a Max Heap.
  left_heap = MaxHeap()

  # Right heap is a Min Heap.
  right_heap = MinHeap()

  # Initial median value is None.
  median = None

  for element in arr:
    median = track_median(element, left_heap, right_heap, median)
    print(median)

  assert median == 10.5


if __name__ == '__main__':
  test_min_heap()
  test_max_heap()

  test_track_median()
