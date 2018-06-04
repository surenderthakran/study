#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class Node(object):
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

  def __repr__(self):
    return repr(self.data)


class DoublyLinkedList(object):
  def __init__(self):
    self.head = None

  def __repr__(self):
    nodes = []
    current = self.head
    while current:
      nodes.append(repr(current))
      current = current.next

    return '[' + ','.join(nodes) + ']'

  def append(self, data):
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
    new_node = Node(data)

    if self.head:
      self.head.prev = new_node
      new_node.next = self.head

    self.head = new_node

if __name__ == '__main__':
  list = [3,5,7,9]

  linked_list = DoublyLinkedList()

  for ele in list:
    linked_list.append(ele)
  print(linked_list)

  linked_list.prepend(1)
  print(linked_list)
