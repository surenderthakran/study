#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from enum import Enum

class Size(Enum):
  S = 1
  M = 2
  L = 3
  XL = 4

class Vehicle(object):
  def __init__(self, license_plate, size):
    self.license_plate = license_plate
    self.size = size


class Slot(object):
  def __init__(self, number, size):
    self.number = number
    self.size = size
    self.occupied = None
    self.occupied_at = None


class ParkingLot(object):
  def __init__(self, id):
    self.id = id


if __name__ == '__main__':
  pass
