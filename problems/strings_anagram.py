#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Check if two given strings are anagrams.

The below implementation operates with an O(n) time complexity.

Usage:
$ python strings_anagram.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def anagram(str1, str2):
  """Checks if two strings are anagrams.

  Args:
    str1: (string)
    str2: (string)

  Returns:
    True if two strings are anagrams else False.
  """
  # Return False if two strings are of unequal length.
  if len(str1) != len(str2):
    return False

  # Initiate an all zero array whose length is equal to the number of ASCII
  # characters.
  ascii_chars = [0] * 256

  # Increase value at the string's character's index in the ASCII array by 1.
  for char in str1:
    ascii_chars[ord(char)] += 1

  # Decrease value at the string's character's index in the ASCII array by 1.
  for char in str2:
    ascii_chars[ord(char)] -= 1

  # If value at any index is not zero, return False.
  for value in ascii_chars:
    if value != 0:
      return False

  return True


if __name__ == '__main__':
  assert anagram('test', 'ttse') is True
  assert anagram('test', 'ttsw') is False
  assert anagram('testing 123', 'tseit 2gn31') is True
