#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class MaxHeap(object):
  """Class to implenent a max heap with a list."""

  def __init__(self, arr=None):
    if not arr:
      self.arr = []
    else:
      self.arr = []
      for element in arr:
        self.add(element)

  def __repr__(self):
    return str(self.arr)

  def left_index(self, index):
    left_index = 2 * index + 1
    # Check if left index is out of bounds.
    if left_index > len(self.arr) - 1:
      return -1

    return left_index

  def left(self, index):
    left_index = self.left_index(index)

    if left_index < 0:
      return None

    return self.arr[left_index]

  def right_index(self, index):
    right_index = 2 * index + 2
    # Check if right index is out of bounds.
    if right_index > len(self.arr) - 1:
      return -1

    return right_index

  def right(self, index):
    right_index = self.right_index(index)

    if right_index < 0:
      return None

    return self.arr[right_index]

  def parent_index(self, index):
    parent_index = (index - 1) // 2
    # Check if parent index is out of bounds.
    if parent_index < 0:
      return -1

    return parent_index

  def parent(self, index):
    parent_index = self.parent_index(index)

    if parent_index < 0:
      return None

    return self.arr[parent_index]

  def add(self, data):
    self.arr.append(data)
    self.bubble_up_element()

  def bubble_up_element(self, index=None):
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

  def get_data_preorder(self, current=None):
    """Returns tree data inorder.

    Args:
      current: (Node) Root node of the tree/subtree.

    Returns:
      List of integers.
    """
    if not current:
      current = 0

    data = [self.arr[current]]

    if self.left(current):
      data += self.get_data_preorder(self.left_index(current))

    if self.right(current):
      data += self.get_data_preorder(self.right_index(current))

    return data


def create_first_heap_and_assert():
  heap = MaxHeap([35, 33, 42, 10, 14, 19, 27, 44, 26, 31])

  assert heap.get_data_preorder() == [44, 42, 33, 10, 26, 31, 14, 35, 19, 27]


if __name__ == '__main__':
  create_first_heap_and_assert()
