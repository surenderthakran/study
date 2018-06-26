#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize - 1


class Node(object):
  """Class to implement a basic binary tree node."""

  def __init__(self, data):
    self.data = data
    self._left = None
    self._right = None

  def __repr__(self):
    return repr(self.data)

  def left(self):
    return self._left

  def set_left(self, node):
    """Sets left child node.

    Args:
      node: (Node) Node to set as left child.

    Raises:
      ValueError: If the left child's value is greater than the current node.
    """
    if not node:
      return

    if node.data > self.data:
      raise ValueError(
          'Left child\'s value %d cannot be greater than root: %d' %
          (node.data, self.data))

    self._left = node

  def right(self):
    return self._right

  def set_right(self, node):
    """Sets right child node.

    Args:
      node: (Node) Node to set as right child.

    Raises:
      ValueError: If the right child's value is smaller than the current node.
    """
    if not node:
      return

    if node.data < self.data:
      raise ValueError(
          'Right child\'s value %d cannot be less than the root: %d' %
          (node.data, self.data))

    self._right = node


class BinarySearchTree(object):
  """Class to implement a binary search tree."""

  def __init__(self):
    self.root = None

  def get_data_inorder(self, current=None):
    """Returns all the nodes' data in the tree in inorder.

    Args:
      current: Current processing node.

    Returns:
      List of integers.
    """
    if not current:
      current = self.root

    inorder = []
    if current.left():
      inorder += self.get_data_inorder(current.left())

    inorder.append(current.data)

    if current.right():
      inorder += self.get_data_inorder(current.right())

    return inorder

  def find(self, data, current=None):
    """Finds and returns the node in the tree with the given data.

    Args:
      data: (int) Data on the required node.
      current: (Node) Current processing node.

    Returns:
      Node with the given value or None if no such node is found.
    """
    if not current:
      current = self.root

    if current.data == data:
      return current
    elif data < current.data and current.left():
      return self.find(data, current.left())
    elif current.right():
      return self.find(data, current.right())

    return None

  def is_binary_search_tree(
      self, current=None, min_val=MIN_INT, max_val=MAX_INT):
    """Determines if the tree is a true binary search tree.

    For a tree to be a binary search tree, it must be:
    1. A binary tree
    2. The left child should be smaller than the current node.
    3. The right child should be greater than the current node.
    4. Every node in the left subtree should be smaller than the current node.
    5. Every node in the right subtree should be smaller than the current node.

    Simply checking the left and right child's value with the current node is
    not enough since a left child can be smaller than the current node but the
    left child's right child could be greater than its grand parent node.

    One method of checking would be to recursively fetch left and right subtree
    nodes for each element and compare data of nodes from both subtree with the
    current node's data.

    Second more efficient method would be to recursively give each node the
    minimum and maximum range for values that it and its children can have.
    The initial minimum and maximum value for the root node would be the
    maximum system integer limits.

    A third simple way of doing it would be to do an in-order traversal of the
    tree and put the results in an array. If the array is sorted than the tree
    is a binary search tree.

    Args:
      current: Node to start processing from. (Node)
      min_val: Minimum allowed value for all children of the current node.
      max_val: Maximum allowed value for all children of the current node.

    Returns:
      True if the tree is a binary search tree else False. (bool)
    """
    # If no current node is given, start with root as the current node.
    if not current:
      current = self.root

    # If the current node's data is out of bounds, it is not a BST.
    if current.data < min_val or current.data > max_val:
      return False

    is_left_bst = True
    if current.left():
      # Give new bounds for the left subtree. The lower bound remains the same
      # as the current subtree but the upper bound would be one less than the
      # current node's value.
      is_left_bst = self.is_binary_search_tree(current.left(),
                                               min_val, current.data - 1)

    is_right_bst = True
    if current.right():
      # Give new bounds to the right subtree. The upper bound will be same as
      # the current subtree but the lower bould would be one greater than the
      # current node's value.
      is_right_bst = self.is_binary_search_tree(current.right(),
                                                current.data + 1, max_val)

    # return true only if both left and right subtrees are BST.
    return is_left_bst and is_right_bst

  def create_bst_from_preorder(self, preorder):
    if not preorder:
      return None

    if len(preorder) == 1:
      return Node(preorder[0])

    current_node = Node(preorder[0])

    preorder = preorder[1:]
    sentinel = len(preorder)
    for index, _ in enumerate(preorder):
      if preorder[index] > current_node.data:
        sentinel = index
        break

    left_preorder = preorder[:sentinel]
    right_preorder = preorder[sentinel:]

    current_node.set_left(self.create_bst_from_preorder(left_preorder))
    current_node.set_right(self.create_bst_from_preorder(right_preorder))

    return current_node


def create_first_tree_and_assert():
  tree = BinarySearchTree()
  tree.root = Node(5)

  node_3 = Node(3)
  tree.root.set_left(node_3)

  node_2 = Node(2)
  node_3.set_left(node_2)

  node_4 = Node(4)
  node_3.set_right(node_4)

  node_1 = Node(1)
  node_2.set_left(node_1)

  node_8 = Node(8)
  tree.root.set_right(node_8)

  node_7 = Node(7)
  node_8.set_left(node_7)

  node_6 = Node(6)
  node_7.set_left(node_6)

  node_9 = Node(9)
  node_8.set_right(node_9)

  assert tree.find(1) is not None
  assert tree.find(10) is None

  assert tree.is_binary_search_tree() is True

  # This is sorted since the tree is a binary search tree.
  assert tree.get_data_inorder() == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def create_second_tree_and_assert():
  tree = BinarySearchTree()
  tree.root = Node(3)

  node_2 = Node(2)
  tree.root.set_left(node_2)

  node_1 = Node(1)
  node_2.set_left(node_1)

  node_4 = Node(4)
  node_2.set_right(node_4)

  node_5 = Node(5)
  tree.root.set_right(node_5)

  assert tree.is_binary_search_tree() is False

  # This is not sorted since it is not a binary search tree.
  assert tree.get_data_inorder() == [1, 2, 4, 3, 5]


if __name__ == '__main__':
  create_first_tree_and_assert()
  create_second_tree_and_assert()

  bst = BinarySearchTree()
  bst.root = bst.create_bst_from_preorder([10, 5, 1, 7, 40, 50])
  assert bst.get_data_inorder() == [1, 5, 7, 10, 40, 50]
