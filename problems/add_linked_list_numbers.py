#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Add two numbers represented in linked lists with one digit per node.

Given two numbers represented by two linked lists with each digit of the
numbers in a separate node. The digits are stored in reverse order, i.e. the
least significant digit is at the lists' head.
Form a third similar linked list which represents the sum of the two numbers.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  """Node implements a node in a single linked list."""
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return repr(self.data)


class LinkedList(object):
  """LinkedList implements a single linked list."""

  def __init__(self):
    self.head = None

  def __repr__(self):
    nodes = []

    if not self.head:
      return nodes

    current = self.head

    while current:
      nodes.append(current)
      current = current.next

    return repr(nodes)

  def append(self, data):
    """Adds a new node at the end of the linked list."""
    node = Node(data)

    if not self.head:
      self.head = node
      return

    current = self.head

    while current.next:
      current = current.next

    current.next = node


def add_linked_list(l1, l2):
  """Adds digits in two linked lists and returns a third with the result."""
  current1 = l1.head
  current2 = l2.head

  result = LinkedList()

  carry = 0

  while current1 and current2:
    digit1 = current1.data or 0
    digit2 = current2.data or 0

    summation = digit1 + digit2 + carry

    if summation > 9:
      carry = 1
      summation = summation % 10

    result.append(summation)

    current1 = current1.next
    current2 = current2.next

  return result

if __name__ == '__main__':
  list1 = LinkedList()
  list1.append(3)
  list1.append(1)
  list1.append(5)

  list2 = LinkedList()
  list2.append(5)
  list2.append(9)
  list2.append(2)

  assert repr(add_linked_list(list1, list2)) == '[8, 0, 8]'
