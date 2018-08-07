#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Find nth last element from a singly linked list.

Before we try to find the nth last element in the linked list, we assume that
the linked list has atleast n elements.

To find the nth last element:
1. Create two pointers p1 and p2.
2. Move p2 forward n-1 times till p1 and p2 are n-1 nodes apart.
3. Move both p1 and p2 forward simultaneously while p2 is not pointing the last
   node.
4. p1 is the nth last node in the linked list.

Usage:
$ python nth_last_linked_list.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  """Node implements a node in a singly linked list."""

  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return repr(self.data)


class SinglyLinkedList(object):
  """SinglyLinkedList implements a singly linked list."""

  def __init__(self, arr=None):
    self.head = None

    if arr:
      for ele in arr:
        self.append(ele)

  def __repr__(self):
    nodes = []
    current = self.head

    while current:
      nodes.append(current)
      current = current.next

    return repr(nodes)

  def append(self, data):
    """Appends a new node to the end of the linked list."""
    node = Node(data)

    if not self.head:
      self.head = node
      return

    current = self.head

    while current.next:
      current = current.next

    current.next = node

  def nth_last(self, n):
    """Returns the nth last node's value."""
    p1 = self.head
    p2 = self.head

    for _ in range(n-1):
      p2 = p2.next

    while p2.next:
      p2 = p2.next
      p1 = p1.next

    return p1.data


if __name__ == '__main__':
  linked_list = SinglyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])

  assert linked_list.nth_last(1) == 9
  assert linked_list.nth_last(2) == 8
  assert linked_list.nth_last(6) == 4
