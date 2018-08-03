#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Write algorithm to rotate a given NxN matrix 90 degrees clockwise.

We approach this problem by rotating each concentric square layer of the matrix
beginning from the outermost layer.
For each layer we identify first and last index of the matrix's range.
A second internal loop rotates every cell of the layer in the previously
determined range.

For a matrix of dimension n*n, the algorithm operates in an O(n^2) time
complexity.

Usage:
$ python rotate_matrix_90_degrees.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def rotate(matrix):
  """Rotates a given NxN matrix clockwise 90 degrees."""
  dimension = len(matrix[0])
  # loop over layers of the matrix to rotate.
  for layer in range(dimension//2):
    first = layer
    last = dimension - 1 - layer


    # shift cells in the current layer clockwise.
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
  input_matrix = [
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

  rotate(input_matrix)

  assert input_matrix == want
