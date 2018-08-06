#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Check if two strings are rotations of each other with a single substring
check.

Two strings s1 and s2 can are rotation of each other if:
1. Both have equal length and
2. The super-string created from concatenating one string twice has the other
   strign as substring.

Usage:
$ python is_rotation.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def is_substring(s1, s2):
  return s1 in s2


def is_rotation(s1, s2):
  if len(s1) != len(s2):
    return False

  str1 = s1 + s1

  return is_substring(s2, str1)


if __name__ == '__main__':
  assert is_rotation('waterbottle', 'erbottlewat') is True
  assert is_rotation('waterbottle', 'bottle') is False
