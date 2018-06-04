#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implement a single-linked list.

Usage:
$ python singly_linked_list.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  """Class to implement a node in a singly-linked list."""

  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    """Returns string representation of the node."""
    return repr(self.data)


class SingleLinkedList(object):
  """Class to implement a singly-linked list."""

  def __init__(self):
    self.head = None

  def __repr__(self):
    """Returns a string representation of the linked list."""
    nodes = []
    current = self.head
    while current:
      nodes.append(repr(current))
      current = current.next

    return '[' + ','.join(nodes) + ']'

  def append(self, data):
    """Appends a new node at the end of the linked list.

    Args:
      data: element for the new node.
    """
    new_node = Node(data)

    if not self.head:
      self.head = new_node
      return

    last_node = self.head
    while last_node.next:
      last_node = last_node.next

    last_node.next = new_node

  def prepend(self, data):
    """Prepends a new node to the beginning of the linked list.

    Args:
      data: element for the new node.
    """
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

  def find(self, data):
    """Returns index of the node in the linked list for the given element.

    Args:
      data: element to find in the linked list.

    Returns:
      integer index of the node or -1 if the element doesn't exists in the
      linked list.
    """
    index = 0
    current = self.head
    while current:
      if current.data == data:
        return index
      index += 1
      current = current.next

    return -1

  def insert(self, data, index):
    """Insert a new node in the linked list at the given index.

    Args:
      data: element for the new node.
      index: position of the new node.

    Returns:
      True if the new node is inserted else False.
    """
    if index == 0:
      self.prepend(data)
      return

    current_index = 0
    current = self.head
    previous = None

    while current:
      if current_index == index:
        new_node = Node(data)
        new_node.next = current
        previous.next = new_node
        return True

      previous = current
      current = current.next
      current_index += 1

    return False

  def delete(self, index):
    """Deletes the node at the given index.

    Args:
      index: index of the node to be removed from the linked list.
    """
    if index == 0 and self.head is not None:
      self.head = self.head.next
      return

    current_index = 0
    current = self.head
    previous = None

    while current:
      if current_index == index:
        previous.next = current.next

      previous = current
      current = current.next
      current_index += 1

if __name__ == '__main__':
  arr = [1, 3, 6, 8, 0]

  linked_list = SingleLinkedList()

  for element in arr:
    linked_list.append(element)

  print('After appeding:', linked_list)

  linked_list.prepend(5)
  print('After prepending', linked_list)

  print('Find 6:', linked_list.find(6))
  print('Find 7:', linked_list.find(7))

  linked_list.insert(2, 2)
  print('After inserting:', linked_list)

  linked_list.insert(4, 0)
  print('After inserting:', linked_list)

  linked_list.delete(1)
  print('After deleting:', linked_list)

  linked_list.delete(0)
  print('After deleting:', linked_list)
