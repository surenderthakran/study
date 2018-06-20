#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import time
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
    self.slot = None


class Slot(object):

  def __init__(self, number, size):
    self.number = number
    self.size = size
    self.occupied = False
    self.occupied_at = None
    self.vehicle = None


class ParkingLot(object):
  # TODO(surenderthakran): Make ParkingLot singleton.

  charges = {
      Size.S.name: 10,
      Size.M.name: 15,
      Size.L.name: 20,
      Size.XL.name: 25,
  }

  def __init__(self, lot_id):
    self.id = lot_id
    self.slots = {
        Size.S.name: [],
        Size.M.name: [],
        Size.L.name: [],
        Size.XL.name: [],
    }
    self.vehicles = {}
    self._initSlots()

  def _InitSlots(self):
    for i in range(100):
      self.slots[Size.S.name].append(Slot(i, Size.S))

    for i in range(100, 200):
      self.slots[Size.M.name].append(Slot(i, Size.M))

    for i in range(200, 300):
      self.slots[Size.L.name].append(Slot(i, Size.L))

    for i in range(300, 400):
      self.slots[Size.XL.name].append(Slot(i, Size.XL))

  def _GetEmptySlot(self, size):
    current_slot_size = size
    slots = self.slots[current_slot_size.name]
    while slots:
      for slot in slots:
        if not slot.occupied:
          return slot
      new_slot_value = current_slot_size.value + 1
      if Size(new_slot_value).name in self.slots:
        slots = self.slots[Size(new_slot_value).name]
        continue
      slots = None

  def _CalculateCharges(self, vehicle):
    slot = vehicle.slot
    exit_time = (time.time())
    duration_in_seconds = exit_time - slot.occupied_at
    duration_in_hours = math.ceil(duration_in_seconds / 3600)
    return type(self).charges[vehicle.size.name] * duration_in_hours

  def ParkVehicle(self, license_plate, size):
    vehicle = Vehicle(license_plate, size)
    slot = self._getEmptySlot(vehicle.size)
    if not slot:
      return False

    slot.occupied = True
    slot.occupied_at = int(time.time())
    slot.vehicle = vehicle
    vehicle.slot = slot
    self.vehicles[vehicle.license_plate] = vehicle
    return True

  def ExitVehicle(self, license_plate):
    vehicle = self.vehicles[license_plate]
    print('Collect: ', self._calculateCharges(vehicle))
    vehicle.slot.occupied_at = None
    vehicle.slot.vehicle = None
    vehicle.slot.occupied = False
    del self.vehicles[license_plate]

  def DisplayAvailability(self):
    small = len(
        [True for slot in self.slots[Size.S.name] if not slot.occupied])
    medium = len(
        [True for slot in self.slots[Size.M.name] if not slot.occupied])
    large = len(
        [True for slot in self.slots[Size.L.name] if not slot.occupied])
    extra_large = len(
        [True for slot in self.slots[Size.XL.name] if not slot.occupied])
    print('S:', small, 'M:', medium, 'L:', large, 'XL:', extra_large)


if __name__ == '__main__':
  parking_lot = ParkingLot(1)
  parking_lot.parkVehicle('IND007', Size.M)
  parking_lot.displayAvailability()
  parking_lot.exitVehicle('IND007')
  parking_lot.displayAvailability()
