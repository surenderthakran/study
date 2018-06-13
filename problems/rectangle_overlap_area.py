#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Given two rectangles, determine the area of their overlap.

For each rectangle we have bottom-left and top-right coordinates.
The rectangles can be anywhere in the 2D cartesian plane. i.e. any of the
four quadrants.
In the rectangles the x coordinate of the bottom-left point is always smaller
then the x coordinate of top-right and the same if true for y coordinate.
Also, all the edges of the two rectangles are parallel to the x or y axis.

Usage:
For a rectangle whose bottom-left and top-right coordinates are:
r1x1,r1y1 and r1x2,r1y2
& the second rectangle:
r2x1,r2y1 and r2x2,r2y2

$ python rectangle_overlap_area.py r1x1,r1y1 r1x2,r1y2 r2x1,r2y1 r2x2,r2y2

Example:
$ python rectangle_overlap_area.py 1,2 4,5 3,4 7,7
1.0

$ python rectangle_overlap_area.py 1,2 4,5 2,3 7,7
4.0

$ python rectangle_overlap_area.py -5,2 1,5 -2,3 7,7
6.0
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


class Point(object):
  """Class to represent a 2D cartesian point."""

  def __init__(self, x, y):
    self.x = x
    self.y = y


class Rectangle(object):
  """Class to represent a rectangle in a 2D cartesian plane."""

  def __init__(self, bottom_left, top_right):
    if top_right.x <= bottom_left.x or top_right.y <= bottom_left.y:
      raise ValueError(
          'Invalid bottom-left and top-right points:', bottom_left, top_right)

    self.bl = bottom_left
    self.tr = top_right

  def __repr__(self):
    return ('[' + str(self.bl.x) + ',' + str(self.bl.y) + ' ' + str(self.tr.x)
            + ',' + str(self.tr.y) + ']')

  def area(self):
    """Calculate area of the rectangle."""
    return (self.tr.x - self.bl.x) * (self.tr.y - self.bl.y)


def overlap_area(r1, r2):
  """Determine if the two rectangles overlap and calculate their overlap area.

  Args:
    r1: Rectangle object of first rectangle.
    r2: Rectangle object of second rectangle.

  Returns:
    Float area of the overlap or -1 if they don't overlap.
  """
  # assuming that the two rectangles overlap.
  # leftmost x coordinate of the overlap rectangle.
  overlap_left_x = max(r1.bl.x, r2.bl.x)

  # rightmost x coordinate of the overlap rectangle.
  overlap_right_x = min(r1.tr.x, r2.tr.x)

  # the rectangles overlap if the leftmost x is smaller than the rightmost x.
  if overlap_left_x >= overlap_right_x:
    return -1

  # lower y coordinate of the overlap area.
  overlap_lower_y = max(r1.bl.y, r2.bl.y)

  # upper y coordinate of the overlap area.
  overlap_upper_y = min(r1.tr.y, r2.tr.y)

  # the rectangles overlap if the lower y is smaller than the upper y.
  if overlap_lower_y >= overlap_upper_y:
    return -1

  overlap_bl = Point(overlap_left_x, overlap_lower_y)
  overlap_tr = Point(overlap_right_x, overlap_upper_y)

  overlap_rect = Rectangle(overlap_bl, overlap_tr)
  print('Overlap Rectangle:', overlap_rect)

  return overlap_rect.area()

if __name__ == '__main__':
  if len(sys.argv) < 5:
    raise ValueError('Please provide coordinates for both rectangles')

  first_point = sys.argv[1].split(',')
  r1bl = Point(float(first_point[0]), float(first_point[1]))

  second_point = sys.argv[2].split(',')
  r1tr = Point(float(second_point[0]), float(second_point[1]))

  third_point = sys.argv[3].split(',')
  r2bl = Point(float(third_point[0]), float(third_point[1]))

  fourth_point = sys.argv[4].split(',')
  r2tr = Point(float(fourth_point[0]), float(fourth_point[1]))

  rectangle1 = Rectangle(r1bl, r1tr)
  rectangle2 = Rectangle(r2bl, r2tr)

  print('Overlap Area:', overlap_area(rectangle1, rectangle2))
