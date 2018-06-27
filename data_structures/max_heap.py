#!/usr/env/bin python2
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  """Class to implement a heap node."""

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None


class MaxHeap(object):
  """Class to implenent a max heap."""

  def __init__(self):
    self.root = None

  def height(self):
    pass

  def create_max_heap_from_list(self, arr):
    pass


def create_first_heap_and_assert():
  heap = MaxHeap()

  node_44 = Node(44)
  heap.root = node_44

  node_42 = Node(42)
  node_44.left = node_42
  node_42.parent = node_44

  node_35 = Node(35)
  node_44.right = node_35
  node_35.parent = node_44

  node_33 = Node(33)
  node_42.left = node_33
  node_33.parent = node_42

  node_31 = Node(31)
  node_42.right = node_31
  node_31.parent = node_42

  node_19 = Node(19)
  node_35.left = node_19
  node_19.parent = node_35

  node_27 = Node(27)
  node_35.right = node_27
  node_27.parent = node_35

  node_10 = Node(10)
  node_33.left = node_10
  node_10.parent = node_33

  node_26 = Node(26)
  node_33.right = node_26
  node_26.parent = node_33

  node_14 = Node(14)
  node_31.left = node_14
  node_14.parent = node_31

  assert heap.height() == 4


if __name__ == '__main__':
  create_first_heap_and_assert()

  a = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
