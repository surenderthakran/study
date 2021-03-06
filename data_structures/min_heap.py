#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implements a binary min heap.

Usage:
$ python min_heap.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class MinHeap(object):
  """Class implementing a Min Heap with an array."""

  def __init__(self, arr=None):
    if not arr:
      self.arr = []
      return

    # Assign the given array to the heap array.
    self.arr = arr
    # Heapify the array in-place.
    self.heapify()

  def heap_array(self):
    return self.arr

  def left_index(self, index):
    left_index = 2 * index + 1

    # If left child's index is out of bounds, return -1.
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

    # If right child's index is out of bounds, return -1.
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

    # If parent's index is out of bounds, return -1.
    if parent_index < 0:
      return -1

    return parent_index

  def parent(self, index):
    parent_index = self.parent_index(index)

    if parent_index == -1:
      return None

    return self.arr[parent_index]

  def heapify(self):
    """Heapifies the current heap array in-place."""
    # If the array has only 1 element, then don't heapify.
    if len(self.arr) < 2:
      return

    # Last parent in a complete binary tree is the parent of the last element.
    last_parent_index = self.parent_index(len(self.arr) - 1)

    # Sink down all parents starting from the last parent to the root.
    for parent_index in range(last_parent_index, -1, -1):
      self.sink_down(parent_index)

  def add(self, data):
    # Add element to the end of the array.
    self.arr.append(data)

    # Bubble up the newly added element to its proper position in the heap.
    self.bubble_up(len(self.arr) - 1)

  def bubble_up(self, index):
    """Bubbles up an element at the given index to its proper position.

    Args:
      index: (int) Index of the element in the heap to bubble up.
    """
    # While the index has a parent and is smaller than its parent.
    while self.parent(index) and self.parent(index) > self.arr[index]:

      # Swap values with parent.
      temp = self.parent(index)
      self.arr[self.parent_index(index)] = self.arr[index]
      self.arr[index] = temp

      # Set index as parent's index to get it bubbled up.
      index = self.parent_index(index)

  def remove(self):
    """Removes the element at the root and re-heapifies the heap.

    Returns:
      (int) Heap's root value if it exists else None.
    """
    # Return if heap has no elements.
    if not self.arr:
      return None

    # Keep root element aside.
    top = self.arr[0]

    # Update root's value as last element.
    self.arr[0] = self.arr[-1]

    # Remove last element from array.
    self.arr = self.arr[:-1]

    # Sink down the root's new value to its proper position.
    self.sink_down(0)

    # Return root's initial value.
    return top

  def sink_down(self, index):
    """Sinks down an element at the given index to its proper position.

    Args:
      index: (int) Index of the element to sink down in the heap.
    """
    while True:
      smallest_index = index

      if self.left(index) and self.left(index) < self.arr[smallest_index]:
        smallest_index = self.left_index(index)

      if self.right(index) and self.right(index) < self.arr[smallest_index]:
        smallest_index = self.right_index(index)

      if smallest_index == index:
        break

      temp = self.arr[index]
      self.arr[index] = self.arr[smallest_index]
      self.arr[smallest_index] = temp

      index = smallest_index

  def delete(self, index):
    """Deletes element from the given index and re-heapifies the heap.

    Args:
      index: (int)  Index of the element to delete from the heap's array.
    """
    # Return if index is out of bounds.
    if index > len(self.arr) - 1 or index < 0:
      return

    # Simply remove last element if index is the last element in the array.
    if index == len(self.arr) - 1:
      self.arr = self.arr[:-1]
      return

    # Update value at index with value of the last element.
    self.arr[index] = self.arr[-1]

    # Remove last element from the array.
    self.arr = self.arr[:-1]

    # Sink down he new value at index to its proper position.
    self.sink_down(index)

if __name__ == '__main__':
  heap = MinHeap([35, 33, 42, 10, 14, 19, 27, 44, 26, 31])

  assert heap.heap_array() == [10, 14, 19, 26, 31, 42, 27, 44, 33, 35]

  assert heap.remove() == 10

  assert heap.heap_array() == [14, 26, 19, 33, 31, 42, 27, 44, 35]

  # Deleting out of bounds index.
  heap.delete(9)

  assert heap.heap_array() == [14, 26, 19, 33, 31, 42, 27, 44, 35]

  # Deleting last index.
  heap.delete(8)

  assert heap.heap_array() == [14, 26, 19, 33, 31, 42, 27, 44]

  heap.delete(2)

  assert heap.heap_array() == [14, 26, 27, 33, 31, 42, 44]

  heap.add(15)

  assert heap.heap_array() == [14, 15, 27, 26, 31, 42, 44, 33]
