#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  def __init__(self, data):
    self.data = data
    self._left = None
    self._right = None

  def Left(self):
    return self._left

  def SetLeft(self, data):
    if data > self.data:
      raise ValueError(
          'Left child\'s value %d cannot be greater than root: %d',
          data, self.data)

    self._left = Node(data)

  def Right(self):
    return self._right

  def SetRight(self, data):
    if data < self.data:
      raise ValueError('Right child\'s value', data,
                       'cannot be less than the root:', self.data)


class BinarySearchTree(object):
  def __init__(self):
    self.root = None

if __name__ == '__main__':
  tree = BinarySearchTree()
  tree.root = Node(5)

  tree.root.SetRight(6)
