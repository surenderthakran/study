#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implement a binary tree.

Usage:
$ python binary_tree.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Queue(object):
  """Class to implement a basic FIFO queue."""

  def __init__(self):
    self.queue = []

  def push(self, ele):
    self.queue.append(ele)

  def pop(self):
    if not self.queue:
      return

    result = self.queue[0]
    self.queue = self.queue[1:]

    return result


class Node(object):
  """Class to implement a node in a binary tree."""

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __repr__(self):
    """Returns string represenatation of a node."""
    return repr(self.data)


class BinaryTree(object):
  """Class to implement a binary tree."""

  def __init__(self):
    self.root = None

  def preorder(self, current):
    """Traverses and prints nodes of a binary tree in preorder.

    Preorder traversal is a type of depth first traversal where the parent's
    node is processed before the left and the right child.

    Args:
      current: root node of the binary tree or sub-tree.
    """
    print(current.data)

    if current.left:
      self.preorder(current.left)

    if current.right:
      self.preorder(current.right)

  def inorder(self, current):
    """Traverses and prints the nodes of a binary tree in inorder.

    Inorder traversal is a type of depth first traversal where the left child
    of a parent node is processed before the node and then the right child.

    Args:
      current: root node of the binary tree or sub-tree.
    """
    if current.left:
      self.inorder(current.left)

    print(current.data)

    if current.right:
      self.inorder(current.right)

  def postorder(self, current):
    """Traverses and prints the nodes of a binary tree in postorder.

    Postorder traversal is a type of depth first traversal where the node is
    processed after processing first its left and then right child.

    Args:
      current: root node of the binary tree or sub-tree.
    """
    if current.left:
      self.postorder(current.left)

    if current.right:
      self.postorder(current.right)

    print(current.data)

  def breadth_first(self, current, queue):
    print(current.data)

    if current.left:
      queue.push(current.left)

    if current.right:
      queue.push(current.right)

    next = queue.pop()
    if next:
      self.breadth_first(next, queue)

  def get_nodes_at_level(self, current, level):
    """Returns a list of node at a level in a binary tree.

    This method returns a list of nodes a given level below the
    given node.

    Args:
      current: root node of the binary tree or sub-tree.
      level: number of levels down from the given root node.

    Returns:
      list of binary tree nodes.
    """
    nodes = []
    if level == 0:
      nodes.append(current)
    elif level > 0:
      if current.left:
        nodes += self.get_nodes_at_level(current.left, level - 1)
      if current.right:
        nodes += self.get_nodes_at_level(current.right, level - 1)

    return nodes

  def height(self, current):
    """Returns the height of a binary tree.

    It calculates the height of a binary tree down from the given node.

    Args:
      current: root node of the binary tree or sub-tree.

    Returns:
      integer height of the binary tree.
    """
    height = 0

    if current:
      height += 1
      height_left = 0
      height_right = 0

      if current.left:
        height_left = self.height(current.left)

      if current.right:
        height_right = self.height(current.right)

      height += max(height_left, height_right)

    return height

  def is_full_tree(self, current):
    """Determines if a binary tree is a full tree.

    A binary tree is considered to be a binary tree if all its nodes have
    exactly 2 children or no children at all.

    Args:
      current: root node of the binary tree or sub-tree.

    Returns:
      True if the tree is a full tree else False.
    """
    if bool(current.left) != bool(current.right):
      return False

    is_full = True

    if current.left:
      is_full = self.is_full_tree(current.left)

    if not is_full:
      return is_full

    if current.right:
      is_full = self.is_full_tree(current.right)

    return is_full

  def is_complete_tree(self):
    """Determines if a binary tree is a complete binary tree.

    A binary tree is considered complete if it has the maximum possible number
    of nodes at each level, i.e. 2^k where k is the level, except for the last
    level.
    The last level must has all nodes to as left as possible.
    @TODO(surenderthakran): implement check if nodes in the last level are as
    left as possible.

    Returns:
      True if the binary tree is complete else False.
    """
    height = self.height(self.root)

    for level in range(height):
      nodes_at_level = self.get_nodes_at_level(self.root, level)
      if len(nodes_at_level) != pow(2, level) and level < height - 2:
        return False

    return True

  def is_perfect_tree(self):
    """Determines if a binary tree is perfect.

    A binary tree is perfect if all its nodes have exaclty 0 or 2 children and
    at every level it has the maximum possible number of nodes, i.e. 2^k.

    Returns:
      True if the binary tree is complete else False.
    """
    height = self.height(self.root)

    for level in range(height):
      nodes_at_level = self.get_nodes_at_level(self.root, level)
      if len(nodes_at_level) != pow(2, level):
        return False

    return True

if __name__ == '__main__':
  tree = BinaryTree()
  tree.root = Node(1)

  node_2 = Node(2)
  tree.root.left = node_2

  node_3 = Node(3)
  tree.root.right = node_3

  node_4 = Node(4)
  node_2.left = node_4

  node_5 = Node(5)
  node_2.right = node_5

  node_6 = Node(6)
  node_3.left = node_6

  node_7 = Node(7)
  node_3.right = node_7

  print('Preorder:')
  tree.preorder(tree.root)

  print('Inorder:')
  tree.inorder(tree.root)

  print('Postorder:')
  tree.postorder(tree.root)

  print('Breadth First:')
  tree.breadth_first(tree.root, Queue())

  print('Height:', tree.height(tree.root))

  print('Nodes at level 1:', tree.get_nodes_at_level(tree.root, 1))
  print('Nodes at level 2:', tree.get_nodes_at_level(tree.root, 2))

  print('Full Tree:', tree.is_full_tree(tree.root))
  print('Complete Tree:', tree.is_complete_tree())
  print('Perfect Tree:', tree.is_perfect_tree())
