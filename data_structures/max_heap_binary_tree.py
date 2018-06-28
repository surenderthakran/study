#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  """Class to implement a heap node."""

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None

  def __repr__(self):
    return str(self.data)


class MaxHeap(object):
  """Class to implenent a max heap."""

  def __init__(self):
    self.root = None

  def get_data_preorder(self, current=None):
    """Returns tree data inorder.

    Args:
      current: (Node) Root node of the tree/subtree.

    Returns:
      List of integers.
    """
    if not current:
      current = self.root

    nodes = [current.data]

    if current.left:
      nodes += self.get_data_preorder(current.left)

    if current.right:
      nodes += self.get_data_preorder(current.right)

    return nodes

  def height(self, current=None):
    """Calculates height of the heap/binary tree from the given node's level.

    Args:
      current: (Node) Node from which we count levels.

    Returns:
      (int) Count of levels down from the given node.
    """
    if not current:
      current = self.root

    left_height = 0
    if current.left:
      left_height = self.height(current.left)

    right_height = 0
    if current.right:
      right_height = self.height(current.right)

    child_height = max(left_height, right_height)

    return child_height + 1

  def get_nodes_at_level(self, level, current=None):
    if not current:
      current = self.root

    if level == 0:
      return [current]

    nodes = []
    if current.left:
      nodes += self.get_nodes_at_level(level-1, current.left)

    if current.right:
      nodes += self.get_nodes_at_level(level-1, current.right)

    return nodes


def create_max_heap_from_list(arr):
  heap = None
  for ele in arr:
    current = Node(ele)
    if not heap:
      heap = MaxHeap()
      heap.root = current
    else:
      height = heap.height()
      insertion_nodes = None
      prev_level_nodes = None
      for level in range(height):
        level_nodes = heap.get_nodes_at_level(level)
        if len(level_nodes) == pow(2, level) and level == height - 1:
          insertion_nodes = level_nodes
          break
        elif len(level_nodes) < pow(2, level):
          insertion_nodes = prev_level_nodes
          break
        prev_level_nodes = level_nodes

      for node in insertion_nodes:
        if not node.left:
          node.left = current
          current.parent = node
          break

        if not node.right:
          node.right = current
          current.parent = node
          break

    max_heapify(current)

  return heap


def max_heapify(current):
  if current.parent and current.data > current.parent.data:
    temp = current.data
    current.data = current.parent.data
    current.parent.data = temp
    max_heapify(current.parent)


def create_first_heap_and_assert():
  heap = MaxHeap()

  node_44 = Node(44)
  heap.root = node_44

  node_42 = Node(42)
  node_44.left = node_42
  node_42.parent = node_44

  node_35 = Node(35)
  node_44.right = node_35
  node_35.parent = node_44

  node_33 = Node(33)
  node_42.left = node_33
  node_33.parent = node_42

  node_31 = Node(31)
  node_42.right = node_31
  node_31.parent = node_42

  node_19 = Node(19)
  node_35.left = node_19
  node_19.parent = node_35

  node_27 = Node(27)
  node_35.right = node_27
  node_27.parent = node_35

  node_10 = Node(10)
  node_33.left = node_10
  node_10.parent = node_33

  node_26 = Node(26)
  node_33.right = node_26
  node_26.parent = node_33

  node_14 = Node(14)
  node_31.left = node_14
  node_14.parent = node_31

  assert heap.height() == 4

  assert repr(heap.get_nodes_at_level(0)) == '[44]'
  assert repr(heap.get_nodes_at_level(1)) == '[42, 35]'
  assert repr(heap.get_nodes_at_level(2)) == '[33, 31, 19, 27]'
  assert repr(heap.get_nodes_at_level(3)) == '[10, 26, 14]'
  assert repr(heap.get_nodes_at_level(4)) == '[]'

  assert heap.get_data_preorder() == [44, 42, 33, 10, 26, 31, 14, 35, 19, 27]


def create_second_heap_and_assert():
  a = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]

  heap = create_max_heap_from_list(a)

  assert heap.height() == 4

  assert repr(heap.get_nodes_at_level(0)) == '[44]'
  assert repr(heap.get_nodes_at_level(1)) == '[42, 35]'
  assert repr(heap.get_nodes_at_level(2)) == '[33, 31, 19, 27]'
  assert repr(heap.get_nodes_at_level(3)) == '[10, 26, 14]'
  assert repr(heap.get_nodes_at_level(4)) == '[]'

  assert heap.get_data_preorder() == [44, 42, 33, 10, 26, 31, 14, 35, 19, 27]


if __name__ == '__main__':
  create_first_heap_and_assert()

  create_second_heap_and_assert()
