#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize - 1


class Node(object):
  def __init__(self, data):
    self.data = data
    self._left = None
    self._right = None

  def __repr__(self):
    return repr(self.data)

  def Left(self):
    return self._left

  def SetLeft(self, node):
    if node.data > self.data:
      raise ValueError(
          'Left child\'s value %d cannot be greater than root: %d' %
          (node.data, self.data))

    self._left = node

  def Right(self):
    return self._right

  def SetRight(self, node):
    if node.data < self.data:
      raise ValueError(
          'Right child\'s value %d cannot be less than the root: %d' %
          (node.data, self.data))

    self._right = node


class BinarySearchTree(object):
  def __init__(self):
    self.root = None

  def find(self, data, current=None):
    if not current:
      current = self.root

    if current.data == data:
      return current
    elif data < current.data and current.Left():
      return self.find(data, current.Left())
    elif current.Right():
      return self.find(data, current.Right())
    else:
      return None

  def is_binary_search_tree(self, current=None, min=MIN_INT, max=MAX_INT):
    if not current:
      current = self.root

    if current.data < min or current.data > max:
      return False

    is_left_bst = True
    if current.Left():
      is_left_bst = self.is_binary_search_tree(current.Left(), min, current.data - 1)

    is_right_bst = True
    if current.Right():
      is_right_bst = self.is_binary_search_tree(current.Right(), current.data + 1, max)

    return is_left_bst and is_right_bst

def create_first_tree_and_assert():
  tree = BinarySearchTree()
  tree.root = Node(5)

  node_3 = Node(3)
  tree.root.SetLeft(node_3)

  node_2 = Node(2)
  node_3.SetLeft(node_2)

  node_4 = Node(4)
  node_3.SetRight(node_4)

  node_1 = Node(1)
  node_2.SetLeft(node_1)

  node_8 = Node(8)
  tree.root.SetRight(node_8)

  node_7 = Node(7)
  node_8.SetLeft(node_7)

  node_6 = Node(6)
  node_7.SetLeft(node_6)

  node_9 = Node(9)
  node_8.SetRight(node_9)

  print(tree.find(1))
  print(tree.find(10))

  assert tree.is_binary_search_tree() is True


def create_second_tree_and_assert():
  tree = BinarySearchTree()
  tree.root = Node(3)

  node_2 = Node(2)
  tree.root.SetLeft(node_2)

  node_1 = Node(1)
  node_2.SetLeft(node_1)

  node_4 = Node(4)
  node_2.SetRight(node_4)

  node_5 = Node(5)
  tree.root.SetRight(node_5)

  assert tree.is_binary_search_tree() is False

if __name__ == '__main__':
  create_first_tree_and_assert()
  create_second_tree_and_assert()
