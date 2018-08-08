#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return repr(self.data)


class CircularLinkedList(object):
  def __init__(self):
    self.head = None

  def add(self, node):
    self.head = node

  def append(self, node_1, node_2):
    node_1.next = node_2


def create_circular_linked_list():
  linked_list = CircularLinkedList()
  node_1 = Node(1)
  linked_list.add(node_1)

  node_2 = Node(2)
  linked_list.append(node_1, node_2)

  node_3 = Node(3)
  linked_list.append(node_2, node_3)

  node_4 = Node(4)
  linked_list.append(node_3, node_4)

  node_5 = Node(5)
  linked_list.append(node_4, node_5)

  node_6 = Node(6)
  linked_list.append(node_5, node_6)

  node_7 = Node(7)
  linked_list.append(node_6, node_7)

  node_8 = Node(8)
  linked_list.append(node_7, node_8)

  node_9 = Node(9)
  linked_list.append(node_8, node_9)

  linked_list.append(node_9, node_4)

  return linked_list


if __name__ == '__main__':
  circular_list = create_circular_linked_list()
