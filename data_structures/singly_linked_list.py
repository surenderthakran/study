#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __repr__(self):
    return repr(self.data)


class SingleLinkedList:
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

    last_node = self.head
    while last_node.next:
      last_node = last_node.next

    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node

  def find(self, data):
    index = 0
    current = self.head
    while current:
      if current.data == data:
        return index
      index += 1
      current = current.next

    return -1

  def insert(self, data, index):
    if index == 0:
      self.prepend(data)

    current_index = 0
    current = self.head

    while current:
      if current_index == index - 1:
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        return True

      current = current.next
      current_index += 1

    return False

if __name__ == '__main__':
  arr = [1, 3, 6, 8, 0]

  linked_list = SingleLinkedList()

  for element in arr:
    linked_list.append(element)

  print(linked_list)

  linked_list.prepend(5)

  print(linked_list)

  print(linked_list.find(6))

  print(linked_list.find(7))

  linked_list.insert(2, 2)

  print(linked_list)

  linked_list.insert(4, 0)

  print(linked_list)
