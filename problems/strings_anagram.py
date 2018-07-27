#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def anagram(str1, str2):
  if len(str1) != len(str2):
    return False

  ascii_chars = [0] * 256

  for char in str1:
    ascii_chars[ord(char)] += 1

  for char in str2:
    ascii_chars[ord(char)] -= 1

  for value in ascii_chars:
    if value != 0:
      return False

  return True


if __name__ == '__main__':
  assert anagram('test', 'ttse') is True
  assert anagram('test', 'ttsw') is False
