#!/usr/env/bin python2
# -*- coding: utf-8 -*-

"""Return all possible permutations of a given string.

For simplicity assume that all characters are unique in the string.

Usage:
$ python string_permutations.py <string>

Example:
$ python string_permutations.py ab
4
['b', 'ab', 'ba', 'a']

$ python problems/string_permutations.py abc
15
['c', 'bc', 'cb', 'b', 'ac', 'ca', 'abc', 'bac', 'bca', 'acb', 'cab', 'cba',
 'ab', 'ba', 'a']
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys


def get_permutations(string):
  """Returns all possible permutations of the given string.

  Args:
    string: argument to get permutations.

  Returns:
    list of strings
  """
  # if the string length is 1 then it has only one permutation.
  if len(string) == 1:
    return [string]

  # Recursive call to get permutations of the string without the first char.
  pems = get_permutations(string[1:])

  # Create new permutations list for permutations because we need to iterate
  # and append to the existing permutations which we put us in an infinite
  # loop.
  new_pems = []

  # Iterate over the known permutations.
  for p in pems:

    # Loop over 1 plus the length of the permutation string.
    # We add 1 to the length so that we can insert the remaining first char
    # at all the positions.
    for i in range(len(p) + 1):

      # insert the remaining first char at the present location in the loop.
      new_pems.append(p[:i] + string[:1] + p[i:])

  # Append the remaining first character to the list of new permutations so
  # that the first characters left behind in every recursive call will also
  # be added as permutations.
  # This step comes after inserting the first char in the existing permutations
  # so that the first character does not inserts to a permutation which had
  # only the first character.
  new_pems.append(string[:1])

  # add the new permutations to the existing list of permutations.
  pems.extend(new_pems)

  return pems

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise ValueError('No input string found')

  arg = sys.argv[1]

  permutations = get_permutations(arg)

  print(len(permutations))
  print(permutations)
