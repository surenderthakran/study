#!/usr/env/bin python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


def get_permutations(str):
  if len(str) == 1:
    return [str]

  pem = []

  char = str[:1]
  rem = str[1:]

  pem.extend(get_permutations(rem))

  pem.append(char)

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise ValueError('No input string found')

  arg = sys.argv[1]

  print(get_permutations(arg))
