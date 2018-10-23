#!usr/bin/env python2
# -*- coding: utf-8 -*-

"""Given a 2D matrix, traverse the matrix in a zigzag manner.

Usage:
$ python 2d_zigzag_scan.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Matrix(object):
  """Class representing a 2D matrix."""

  def __init__(self, matrix):
    self.matrix = matrix
    self.x_len = len(matrix)
    self.y_len = len(matrix[0])
    self.cursor_pos = [0, 0]
    self.prev_move = None

  def get_cursor_value(self):
    return self.matrix[self.cursor_pos[0]][self.cursor_pos[1]]

  def count_elements(self):
    return len(self.matrix) * len(self.matrix[0])

  def move_right(self):
    if self.cursor_pos[1] < self.y_len - 1:
      self.cursor_pos[1] += 1
      self.prev_move = 'right'
      return True

    return False

  def move_bottom(self):
    if self.cursor_pos[0] < self.x_len - 1:
      self.cursor_pos[0] += 1
      self.prev_move = 'bottom'
      return True

    return False

  def move_bottom_left(self):
    if self.cursor_pos[1] > 0 and self.cursor_pos[0] < self.x_len - 1:
      self.cursor_pos[0] += 1
      self.cursor_pos[1] -= 1
      self.prev_move = 'bottom_left'
      return True

    return False

  def move_top_right(self):
    if self.cursor_pos[0] > 0 and self.cursor_pos[1] < self.y_len - 1:
      self.cursor_pos[0] -= 1
      self.cursor_pos[1] += 1
      self.prev_move = 'top_right'
      return True

    return False

  def zigzag(self):
    """Traverses the matrix in zigzag order.

    Returns:
      List of matrix elements.
    """
    res = [self.get_cursor_value()]
    total_elements = self.count_elements()

    # Traverse until all elements are traversed.
    while len(res) < total_elements:
      # If previous move was None attempt to move in right or bottom direction.
      if self.prev_move is None:
        if not self.move_right():
          self.move_bottom()
      # If previous move was towards right, try to move to bottom-left
      # direction.
      elif self.prev_move == 'right':
        self.move_bottom_left()
      # If previous move was towards bottom-left, try moving to bottom-left,
      # bottom or right.
      elif self.prev_move == 'bottom_left':
        if not self.move_bottom_left():
          if not self.move_bottom():
            self.move_right()
      # If previous move was to bottom, try moving top-right or bottom-left.
      elif self.prev_move == 'bottom':
        if not self.move_top_right():
          self.move_bottom_left()
      # If previous move was to top-right, try moving to top-right, right or
      # bottom.
      elif self.prev_move == 'top_right':
        if not self.move_top_right():
          if not self.move_right():
            self.move_bottom()

      # Append current element to the response list.
      res.append(self.get_cursor_value())

    return res


if __name__ == '__main__':
  mtrx = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  zigzag = mtrx.zigzag()

  assert zigzag == [1, 2, 4, 7, 5, 3, 6, 8, 9]
