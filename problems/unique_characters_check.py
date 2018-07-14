#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Check if a string has all unique characters.
Without using any additional data structures.

Usage:
$ python unique_characters_check.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def is_unique_chars(string):
  """Checks if the given string has all unique characters.

  Args:
    string: (string)

  Returns:
    True if all characters are unique else False.
  """
  # Let us assume that the string only has ASCII characters.
  # Create an array of all False elements whose length is equal to the number
  # of ASCII characters.
  chars = [False] * 256

  # For every character in the string.
  for char in string:
    # If the value at the index equal to the character's ASCII value in the
    # array is True, it has already been encountered in the string.
    if chars[ord(char)]:
      return False

    # Set value as True in the array at index equal to the ASCII value of the
    # character.
    chars[ord(char)] = True

  return True


if __name__ == '__main__':
  assert is_unique_chars('abcdef') is True
  assert is_unique_chars('abcdefa') is False
