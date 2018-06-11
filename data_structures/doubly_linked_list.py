#!/usr/bin/env python2
# -*- coding:utf-8 -*-

"""Implement a doubly linked list.

Usage:
$ python doubly_linked_list.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  """Class to implement a node in a double linked list."""

  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

  def __repr__(self):
    """Returns the string representation of the node."""
    return repr(self.data)


class DoublyLinkedList(object):
  """Class to implement a doubly linked list."""

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
      data: for the new node.
    """
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return

    last = self.head
    while last.next:
      last = last.next

    last.next = new_node
    new_node.prev = last

  def prepend(self, data):
    """Appends a new node at the beginning of the linked list.

    Args:
      data: for the new node.
    """
    new_node = Node(data)

    if self.head:
      self.head.prev = new_node
      new_node.next = self.head

    self.head = new_node

  def find(self, data):
    """Returns the location of the element in the linked list.

    Args:
      data: to search in the linked list.

    Returns:
      integer position of the data of -1 if the element does not exists.
    """
    current = self.head
    index = 0
    while current:
      if current.data == data:
        return index
      index += 1
      current = current.next

    return -1

  def insert(self, data, index):
    """Inserts a new node at the given position in the linked list.

    Args:
      data: for the new node.
      index: to insert the node at.
    """
    if index == 0:
      self.prepend(data)
      return

    current = self.head
    current_index = 0
    previous = None
    while current or previous:
      if current_index == index:
        new_node = Node(data)

        new_node.next = current
        new_node.prev = previous

        previous.next = new_node
        if current:
          current.prev = new_node

        return

      previous = current
      current = current.next
      current_index += 1

    return

  def delete(self, index):
    """Removes the node at the given index from the linked list.

    Args:
      index: of the node to be removed.
    """
    if index == 0:
      self.head = self.head.next
      return

    current_index = 0
    current = self.head
    while current:
      if current_index == index:
        current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev

        current.next = None
        current.prev = None
        return

      current = current.next
      current_index += 1

    return

if __name__ == '__main__':
  arr = [3, 5, 7, 9]

  linked_list = DoublyLinkedList()

  for ele in arr:
    linked_list.append(ele)
  print('After append:', linked_list)

  linked_list.prepend(1)
  print('After prepend:', linked_list)

  print('Find:', linked_list.find(5))
  print('Find:', linked_list.find(6))

  linked_list.insert(4, 2)
  print('After insert:', linked_list)

  linked_list.insert(0, 0)
  print('After insert:', linked_list)

  linked_list.insert(10, 7)
  print('After insert:', linked_list)

  linked_list.delete(0)
  print('After delete:', linked_list)

  linked_list.delete(6)
  print('After delete:', linked_list)

  linked_list.delete(2)
  print('After delete:', linked_list)
