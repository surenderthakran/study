#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Design a system for a parking lot.

Assuming there are four sizes of slots in the parking lot for four different
sizes of vehicles.
If no empty slot can be found for a vehicle's size, the vehicle can be
upgraded to a larger size slot.

Even if an instance of ParkingLot class is created at each of the multiple
entry/exit point of the parking lot, they should all be looking at the same
slot and vehicle data.

Usage:
$ python parking_lot.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import random
import time
from enum import Enum


class Size(Enum):
  """Enum to hold sizes in the system."""
  small = 1
  medium = 2
  large = 3
  extra_large = 4


class Queue(object):
  """Class to implement a basic FIFO queue."""

  def __init__(self):
    self.queue = []

  def __iter__(self):
    """Implementing the iter magic method to make Queue iterable."""
    return iter(self.queue)

  def Push(self, ele):
    """Adds an element to the queue.

    Args:
      ele: Element to add to the queue.
    """
    self.queue.append(ele)

  def Pop(self):
    """Removes an element from the queue.

    Returns:
      The oldest element in the queue or None if the queue is empty.
    """
    if not self.queue:
      return None

    ele = self.queue[0]
    self.queue = self.queue[1:]

    return ele


class Vehicle(object):
  """Class to encapsulate a vehicle's properties."""

  def __init__(self, license_plate, size):
    self.license_plate = license_plate
    self.size = size
    self.slot = None


class Slot(object):
  """Class to encapsulate a parking slot's properties."""

  def __init__(self, number, size):
    self.number = number
    self.size = size
    self.occupied = False
    self.occupied_at = None
    self.vehicle = None


class ParkingLot(object):
  """Class to encapsulate and implement a parking lot."""

  # Flag to signify if the class variables have already been initialized while
  # creating a previous instance of the class.
  initialized = False

  # Holds instances of slots in a dict against their sizes.
  slots = {}

  # Dictionary to hold objects of vehicles parked in the parking lot against
  # license plate numbers.
  vehicles = {}

  # Hourly parking charges for each slot size.
  charges = {
      Size.small.name: 10,
      Size.medium.name: 15,
      Size.large.name: 20,
      Size.extra_large.name: 25,
  }

  # Total money collected from parking charges.
  collection = 0

  def __init__(self):
    # Do not reinitialize slots if they already have been initialized.
    if not type(self).initialized:
      self._InitSlots()

  def _InitSlots(self):
    """Initialize parking slots.

    Creates slot instances for different slot sizes and stores them as a Queue
    in the slots dictionary class variable against there size.
    """
    type(self).slots[Size.small.name] = Queue()
    for i in range(50):
      type(self).slots[Size.small.name].Push(Slot(i, Size.small))

    type(self).slots[Size.medium.name] = Queue()
    for i in range(50, 100):
      type(self).slots[Size.medium.name].Push(Slot(i, Size.medium))

    type(self).slots[Size.large.name] = Queue()
    for i in range(100, 150):
      type(self).slots[Size.large.name].Push(Slot(i, Size.large))

    type(self).slots[Size.extra_large.name] = Queue()
    for i in range(150, 200):
      type(self).slots[Size.extra_large.name].Push(Slot(i, Size.extra_large))

    # Set initialized to True once initialization is complete.
    type(self).initialized = True

  def _GetEmptySlot(self, size):
    """Returns an appropriate empty slot for a vehicle size.

    If no slots of a size are empty, a slot of a higher size is returned.

    Args:
      size: Size of the vehicle.

    Returns:
      A Slot object or None.
    """
    current_slot_size = size

    # Fetch Queue of empty slots for the current slot size.
    slots_queue = type(self).slots[current_slot_size.name]

    # Keep looping until a queue of slots exist.
    while slots_queue:

      # Fetch a slot from the queue and return it.
      slot = slots_queue.Pop()
      if slot:
        return slot

      # If an empty slot of the required size does not exists, determine a
      # higher slot size.
      new_slot_value = current_slot_size.value + 1

      # If a queue of empty slots for the higher slot size doesn't exists,
      # return None.
      if Size(new_slot_value).name not in self.slots:
        return None

      # If a queue of empty slots for the higher slot size exists, set it in a
      # variable to loop again.
      slots_queue = type(self).slots[Size(new_slot_value).name]

  def _CalculateCharges(self, vehicle):
    """Calculates parking charges to be paid.

    Args:
      vehicle: Vehicle object of the vehicle to calculate charges for.

    Returns:
      Parking charge to be paid.
    """
    slot = vehicle.slot
    exit_time = (time.time())
    duration_in_seconds = exit_time - slot.occupied_at
    duration_in_hours = math.ceil(duration_in_seconds / 3600)
    return type(self).charges[vehicle.size.name] * duration_in_hours

  def ParkVehicle(self, license_plate, size):
    """Parks a vehicle in the parking lot.

    Args:
      license_plate: License plate number of the vehicle.
      size: Size enum value for the vehicle's size.

    Returns:
      True if the vehicle is parked else False.
    """
    # Return if a vehicle with the given license plate number is already
    # parked.
    if license_plate in type(self).vehicles:
      return False

    vehicle = Vehicle(license_plate, size)

    # Search an empty slot for the vehicle.
    slot = self._GetEmptySlot(vehicle.size)
    # Return if no slot is found.
    if not slot:
      return False

    # Update slot to mark it occupied.
    slot.occupied = True
    slot.occupied_at = int(time.time())
    slot.vehicle = vehicle

    # Add slot to the vehicle object.
    vehicle.slot = slot

    # Add vehicle to the vehicles dictionary class variable.
    type(self).vehicles[vehicle.license_plate] = vehicle

    return True

  def ExitVehicle(self, license_plate):
    """Exits a vehicle from the parking lot.

    Args:
      license_plate: License plate number of the vehicle to be exited.

    Returns:
      True if the vehicle is exited else False.
    """
    # Check if the vehicle with license plate number is parked in the lot.
    vehicle = type(self).vehicles.pop(license_plate, None)
    if not vehicle:
      return False

    # Collect parking charges.
    type(self).collection += self._CalculateCharges(vehicle)

    # Mark slot as empty.
    vehicle.slot.occupied_at = None
    vehicle.slot.vehicle = None
    vehicle.slot.occupied = False

    # Add slot to the appropriate empty slots Queue in the class variable.
    type(self).slots[vehicle.slot.size.name].Push(vehicle.slot)

    return True

  def DisplayStats(self):
    """Prints the current count of empty slots and parking charges collected."""
    small = len([
        True for slot in type(self).slots[Size.small.name] if not slot.occupied
    ])
    medium = len([
        True for slot in type(self).slots[Size.medium.name] if not slot.occupied
    ])
    large = len([
        True for slot in type(self).slots[Size.large.name] if not slot.occupied
    ])
    extra_large = len([
        True for slot in type(self).slots[Size.extra_large.name]
        if not slot.occupied
    ])
    print('S:', small, 'M:', medium, 'L:', large, 'XL:', extra_large,
          'Total:', small + medium + large + extra_large,
          'Collections:', type(self).collection)


if __name__ == '__main__':
  parking_lot = ParkingLot()

  # Randomly park and exit vehicles.
  for _ in range(500):
    if random.randint(0, 1) == 0:
      # Exit vehicle.
      exited = parking_lot.ExitVehicle(str(random.randint(1, 50)))
      if exited:
        parking_lot.DisplayStats()
    else:
      # Park vehicle.
      parked = parking_lot.ParkVehicle(
          str(random.randint(1, 50)), Size(random.randint(1, 4)))
      if parked:
        parking_lot.DisplayStats()
