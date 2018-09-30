#/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Compare two lists of keypresses for equality.
The lists of keypresses can have only lowercase characters or 'backspace'.

Usage:
python compare_keypress_lists.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def stringify_keypresses(keys):
  """Converts list of keypresses into string.

  Args:
    keys: List of strings depicting keys pressed.

  Returns:
    String
  """
  string = ''
  for key in keys:
    if key == 'backspace':
      string = string[:-1]
    else:
      string += key

  return string


def compare_keypresses(list_1, list_2):
  """Compares two list of keypresses for equality.

  Args:
    list_1: List of strings depicting keys pressed.
    list_2: List fo strings depicting keys pressed.

  Returns:
    True if the two keypress lists equate to same string else False.
  """
  str1 = ''
  if list_1:
    str1 = stringify_keypresses(list_1)

  str2 = ''
  if list_2:
    str2 = stringify_keypresses(list_2)

  return str1 == str2

if __name__ == '__main__':
  assert compare_keypresses(['a', 'b', 'c'],
                            ['a', 'b', 'backspace', 'b', 'c']) is True
  assert compare_keypresses([], ['backspace']) is True
  assert compare_keypresses(
      ['a'], ['backspace', 'a', 'b', 'c', 'backspace', 'backspace']) is True

  assert compare_keypresses(['a', 'b', 'c'],
                            ['a', 'b', 'c', 'backspace', 'd']) is False
