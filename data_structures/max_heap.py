#!/usr/bin/env python2
# -*- coding:utf-8 -*-

"""Implements a Max Binary Heap.

Usage:
$ python max_heap_array.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class MaxHeap(object):
  """Class to implenent a max heap with a list."""

  def __init__(self, arr=None):
    if not arr:
      self.arr = []
    else:
      self.arr = arr
      # Heapify the array in-place.
      self.heapify()

  def __repr__(self):
    return str(self.arr)

  def left_index(self, index):
    """Returns left child's index of the given node if it exists else -1."""
    left_index = 2 * index + 1
    # Check if left index is out of bounds.
    if left_index > len(self.arr) - 1:
      return -1

    return left_index

  def left(self, index):
    """Returns left child of the given node if t exists else None."""
    left_index = self.left_index(index)

    if left_index < 0:
      return None

    return self.arr[left_index]

  def right_index(self, index):

    """Returns right child's index of the given node if it exists else -1."""
    right_index = 2 * index + 2
    # Check if right index is out of bounds.
    if right_index > len(self.arr) - 1:
      return -1

    return right_index

  def right(self, index):
    """Returns right child of the given node if it exists else None."""
    right_index = self.right_index(index)

    if right_index < 0:
      return None

    return self.arr[right_index]

  def parent_index(self, index):
    """Returns parent's index of the given node if it exists else -1."""
    parent_index = (index - 1) // 2
    # Check if parent index is out of bounds.
    if parent_index < 0:
      return -1

    return parent_index

  def parent(self, index):
    """Returns parent of the given node if it exists else None."""
    parent_index = self.parent_index(index)

    if parent_index < 0:
      return None

    return self.arr[parent_index]

  def heap_array(self):
    """Returns the array representing the heap."""
    return self.arr

  def heapify(self):
    """Heapifies the array in-place."""
    if len(self.arr) < 2:
      return

    # The last parent of the heap would be the parent of the last element.
    last_parent = self.parent_index(len(self.arr) - 1)

    # Sink down all parent nodes starting from the last parent.
    for parent in range(last_parent, -1, -1):
      self.sink_down(parent)

  def add(self, data):
    """Adds a new element to the heap.

    The new element is added as the last node in the last level i.e. at the end
    of the heap's arrayn and then bubbled up to its proper position.

    Args:
      data: (int) Element to be added to the heap.
    """
    self.arr.append(data)
    self.bubble_up()

  def bubble_up(self, index=None):
    """Moves an element up the heap levels to its appropriate level.

    Args:
      index: (int) Index of the element in the heap array to be bubbled up.
    """
    # If no index is given, heapify the last element.
    if not index:
      index = len(self.arr) - 1

    # If parent exists and its value is smaller than the current node.
    while self.parent(index) and self.parent(index) < self.arr[index]:
      # Swap with parent
      temp = self.parent(index)
      self.arr[self.parent_index(index)] = self.arr[index]
      self.arr[index] = temp

      # Set parent's index as current index.
      index = self.parent_index(index)

  def remove(self):
    """Removes and returns the root element from the heap.

    Returns:
      The root element in the heap.
    """
    # Locate the root element.
    top = self.arr[0]

    # Replace the root with the last elemrnt.
    self.arr[0] = self.arr[-1]

    # Remove the last element from the array.
    self.arr = self.arr[:-1]

    # Sink down the new value at the root to its proper position.
    self.sink_down(0)

    return top

  def sink_down(self, index):
    """Sinks down the given element to its proper position in the max heap.

    Amongst the parent and its two children, we deduce the largest element,
    and if the parent is not the largest we replace it with the largest child.
    Repeat the same process with the replaced child.

    Args:
      index: (int) Index of the element the array to be sunk down.
    """
    # Start with setting parent as the largest.
    largest = index

    # If left exists and is larger than the largest, set it's index as largest.
    if self.left(index) and self.left(index) > self.arr[largest]:
      largest = self.left_index(index)

    # If right exists and is larger than the largest, set it as largest.
    if self.right(index) and self.right(index) > self.arr[largest]:
      largest = self.right_index(index)

    # If parent is not the largest, swap it with the largest.
    if largest != index:
      temp = self.arr[index]
      self.arr[index] = self.arr[largest]
      self.arr[largest] = temp

      # Repeat with the swapped child as parent.
      self.sink_down(largest)

  def delete(self, index):
    """Deletes the given index element from the heap.

    Args:
      index: (int) Index of the element in the heap array.
    """
    # Return if index is out of bounds.
    if index < 0 or index > len(self.arr) - 1:
      return

    # If the element to be removed is the last element in the heap, simply
    # remove it from the array.
    if index == len(self.arr) - 1:
      self.arr = self.arr[:-1]
      return

    # Replace index with the last element in the heap.
    self.arr[index] = self.arr[-1]

    # Remove last element in the heap.
    self.arr = self.arr[:-1]

    # Sink down the newly replaced element at the index.
    self.sink_down(index)


def create_heap_and_assert():
  """Creates a max heap and runs assertion checks."""
  heap = MaxHeap([35, 33, 42, 10, 14, 19, 27, 44, 26, 31])

  assert heap.heap_array() == [44, 35, 42, 33, 31, 19, 27, 10, 26, 14]

  assert heap.remove() == 44

  assert heap.heap_array() == [42, 35, 27, 33, 31, 19, 14, 10, 26]

  heap.delete(9)

  assert heap.heap_array() == [42, 35, 27, 33, 31, 19, 14, 10, 26]

  heap.delete(2)

  assert heap.heap_array() == [42, 35, 26, 33, 31, 19, 14, 10]

  heap.delete(7)

  assert heap.heap_array() == [42, 35, 26, 33, 31, 19, 14]

  heap.add(40)

  assert heap.heap_array() == [42, 40, 26, 35, 31, 19, 14, 33]

if __name__ == '__main__':
  create_heap_and_assert()
