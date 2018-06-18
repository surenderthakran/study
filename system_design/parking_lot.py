#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from enum import Enum

vehicles = {}

class Size(Enum):
  S = 1
  M = 2
  L = 3
  XL = 4

class Vehicle(object):
  def __init__(self, license_plate, size):
    self.license_plate = license_plate
    self.size = size
    self.slot = None

  def getSlot(self):
    pass


class Slot(object):
  def __init__(self, number, size):
    self.number = number
    self.size = size
    self.occupied = None
    self.occupied_at = None


class ParkingLot(object):
  _instance = None

  def __init__(self, id):
    self.id = id
    self.slots = None
    self.vehicles = {}

  def getEmptySlot(self, size):
    pass

  def parkVehicle(self, vehicle, slot):
    pass

  def exitVehicle(self, vehicle):
    pass


if __name__ == '__main__':
  pass
