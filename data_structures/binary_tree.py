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

  def get_nodes_preorder(self, current=None):
    """Traverses and prints nodes of a binary tree in preorder.

    Preorder traversal is a type of depth first traversal where the parent's
    node is processed before the left and the right child.

    Args:
      current: root node of the binary tree or sub-tree.

    Retruns:
      List of nodes.
    """
    if not current:
      current = self.root

    nodes = [current]

    if current.left:
      nodes += self.get_nodes_preorder(current.left)

    if current.right:
      nodes += self.get_nodes_preorder(current.right)

    return nodes

  def get_nodes_inorder(self, current=None):
    """Traverses and prints the nodes of a binary tree in inorder.

    Inorder traversal is a type of depth first traversal where the left child
    of a parent node is processed before the node and then the right child.

    Args:
      current: root node of the binary tree or sub-tree.

    Returns:
      List of nodes.
    """
    if not current:
      current = self.root

    nodes = []
    if current.left:
      nodes += self.get_nodes_inorder(current.left)

    nodes.append(current)

    if current.right:
      nodes += self.get_nodes_inorder(current.right)

    return nodes

  def get_nodes_postorder(self, current=None):
    """Traverses and prints the nodes of a binary tree in postorder.

    Postorder traversal is a type of depth first traversal where the node is
    processed after processing first its left and then right child.

    Args:
      current: root node of the binary tree or sub-tree.

    Returns:
      List of nodes.
    """
    if not current:
      current = self.root

    nodes = []
    if current.left:
      nodes += self.get_nodes_postorder(current.left)

    if current.right:
      nodes += self.get_nodes_postorder(current.right)

    nodes.append(current)

    return nodes

  def get_nodes_breadth_first(self, current=None, queue=None):
    """Traverses and prints the nodes of a binary tree in level order.

    Level Order or Breadth first traversal is where all the nodes of a level
    are processed before moving on to the next level.

    Args:
      current: Current node to be processed.
      queue: FIFO queue of all the nodes.

    Returns:
      List of nodes.
    """
    if not current:
      current = self.root

    if not queue:
      queue = Queue()

    nodes = [current]

    if current.left:
      queue.push(current.left)

    if current.right:
      queue.push(current.right)

    next_node = queue.pop()
    if next_node:
      nodes += self.get_nodes_breadth_first(next_node, queue)

    return nodes

  def get_nodes_at_level(self, level, current=None):
    """Returns a list of node at a level in a binary tree.

    This method returns a list of nodes a given level below the
    given node.

    Args:
      level: number of levels down from the given root node.
      current: root node of the binary tree or sub-tree.

    Returns:
      list of binary tree nodes.
    """
    if not current:
      current = self.root

    nodes = []
    if level == 0:
      nodes.append(current)
    elif level > 0:
      if current.left:
        nodes += self.get_nodes_at_level(level - 1, current.left)
      if current.right:
        nodes += self.get_nodes_at_level(level - 1, current.right)

    return nodes

  def height(self, current=None):
    """Returns the height of a binary tree.

    It calculates the height of a binary tree down from the given node.

    Args:
      current: root node of the binary tree or sub-tree.

    Returns:
      integer height of the binary tree.
    """
    if not current:
      current = self.root

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

  def is_full_tree(self, current=None):
    """Determines if a binary tree is a full tree.

    A binary tree is considered to be a binary full tree if all its nodes have
    exactly 2 children or no children at all.
    The nodes with no children need not be in the last level.

    Args:
      current: root node of the binary tree or sub-tree.

    Returns:
      True if the tree is a full tree else False.
    """
    if not current:
      current = self.root

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
      nodes_at_level = self.get_nodes_at_level(level)
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
      nodes_at_level = self.get_nodes_at_level(level)
      if len(nodes_at_level) != pow(2, level):
        return False

    return True


def create_tree_and_assert():
  """Creates a binary tree and runs assertions on its methods."""
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

  assert repr(tree.get_nodes_preorder()) == '[1, 2, 4, 5, 3, 6, 7]'

  assert repr(tree.get_nodes_inorder()) == '[4, 2, 5, 1, 6, 3, 7]'

  assert repr(tree.get_nodes_postorder()) == '[4, 5, 2, 6, 7, 3, 1]'

  assert repr(tree.get_nodes_breadth_first()) == '[1, 2, 3, 4, 5, 6, 7]'

  assert tree.height() == 3

  assert repr(tree.get_nodes_at_level(0)) == '[1]'
  assert repr(tree.get_nodes_at_level(1)) == '[2, 3]'
  assert repr(tree.get_nodes_at_level(2)) == '[4, 5, 6, 7]'

  assert tree.is_full_tree() is True
  assert tree.is_complete_tree() is True
  assert tree.is_perfect_tree() is True


if __name__ == '__main__':
  create_tree_and_assert()
