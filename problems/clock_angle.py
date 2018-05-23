#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Calculates the angle between the minute and the hour hand in a clock for a
given time.

Usage:
$ python clock_angle.py <time as a floating number>

ex:
$ python clock_angle.py 09.34
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


def is_valid_time(time):
  if '.' not in time:
    return False

  if time.count('.') > 1:
    return False

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise ValueError('Please enter a time')

  time = sys.argv[1]

  if not is_valid_time(time):
    raise ValueError('time is not valid:', time)
