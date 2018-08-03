#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def rotate(matrix):
  dimension = len(matrix[0])
  for layer in range(dimension//2):
    first = layer
    last = dimension - 1 - layer


    for i in range(first, last):
      top_element = matrix[first][i]

      # left to top.
      matrix[first][i] = matrix[first + last - i][first]

      # bottom to left.
      matrix[first + last - i][first] = matrix[last][first + last - i]

      # right to bottom.
      matrix[last][first + last - i] = matrix[i][last]

      # top to right.
      matrix[i][last] = top_element


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

  rotate(matrix)

  assert matrix == want
