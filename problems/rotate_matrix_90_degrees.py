#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def rotate(matrix):
  dimension = len(matrix[0])
  for layer in range(dimension//2):
    print('rotating layer:', layer)


if __name__ == '__main__':
  matrix = [
      [10, 11, 12, 13, 14],
      [15, 16, 17, 18, 19],
      [20, 21, 22, 23, 24],
      [25, 26, 27, 28, 29],
      [30, 31, 32, 33, 34],
  ]
  want = [
      [30, 25, 20, 15, 10],
      [31, 26, 21, 16, 11],
      [32, 27, 22, 17, 12],
      [33, 28, 23, 18, 13],
      [34, 29, 24, 19, 14],
  ]
  assert rotate(matrix) == want
