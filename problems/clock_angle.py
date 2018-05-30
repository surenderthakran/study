#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Calculate angle between the minute and hour hand in a clock.

Usage:
$ python clock_angle.py <time as a floating number>

Example:
$ python clock_angle.py 10.00
60.0

$ python clock_angle.py 10.15
142.5

$ python clock_angle.py 10.30
135.0

$ python clock_angle.py 12.00
0

$ python clock_angle.py 12.30
165.0

$ python clock_angle.py 6.30
15.0
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


def is_valid_time(time):
  """Checks if the provided time is valid.

  Args:
    time: Time as a float string.

  Returns:
    bool: True if the given time is valid else False.
  """
  if '.' not in time:
    return False

  if time.count('.') > 1:
    return False

  hours, minutes = get_hours_and_minutes(time)

  if hours < 0 or hours > 12 or minutes < 0 or minutes > 59:
    return False

  return True


def get_hours_and_minutes(time):
  """Returns hours and minutes from the time.

  Args:
    time: Time as a float string.

  Returns:
    (int, int): hour and minute as int from the time.
  """
  hours = int(time.split('.')[0])
  # set hours to 0 if it is 12 since we calculate hour hand's angle from the
  # 12th mark.
  hours = 0 if hours == 12 else hours

  minutes = int(time.split('.')[1])

  return hours, minutes


def get_angle_between_hands(hours, minutes):
  """Calculates angle between the hour and minute hands in a clock.

  Args:
    hours: The hours in the time as int.
    minutes: The minutes in the time as int.

  Returns:
    The angle between the hands as float.
  """
  # calculate minute hand's angle with the 12th mark.
  # angle between two consecutive minute marks is 6 degrees in a clock.
  minute_hands_angle_with_root = minutes * 6
  # calculate hour hand's angle with the 12th mark.
  # angle between two consecutive hour marks is 30 degrees in a clock.
  # with each mark increase by the minute hand, the hour hand moves by
  # 30 * 1 / 60 = 1/2 degrees.
  hour_hands_angle_with_root = (hours * 30) + (minutes/2)

  # the angle betwen the hour and the minute hand is the absolute value of
  # difference between their angles with the 12th mark.
  angle = abs(minute_hands_angle_with_root - hour_hands_angle_with_root)

  # convert reflex angle to less than straight angle.
  if angle > 180:
    angle = abs(angle - 360)

  return angle

if __name__ == '__main__':
  # check if time has been provided.
  if len(sys.argv) < 2:
    raise ValueError('Please enter a time')

  time = sys.argv[1]

  # validate time validity
  if not is_valid_time(time):
    raise ValueError('time is not valid:', time)

  hours, minutes = get_hours_and_minutes(time)

  print(get_angle_between_hands(hours, minutes))
