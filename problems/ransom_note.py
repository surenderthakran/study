#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Check if a ransom note can be made by cutting words from a magazine page.

Usage:
$ python ransom_note.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def is_ransom_source(note, magazine):
  # Convert the texts to lower case and transform them into list using python's
  # split() method which will take care of generalizing newline and
  # whitespaces.
  # Also, for the sake of simplicity we are not bothering about the punctuation
  # marks in this solution.
  note_list = note.lower().split()
  magazine_list  = magazine.lower().split()

  # create a dictionary of words in the ransom note against the count of their
  # occurence.
  note_dict = {}
  for word in note_list:
    if word in note_dict:
      note_dict[word] += 1
    else:
      note_dict[word] = 1

  # create similar dictionary for the magazine page.
  magazine_dict = {}
  for word in magazine_list:
    if word in magazine_dict:
      magazine_dict[word] += 1
    else:
      magazine_dict[word] = 1

  # iterate over every unique word in the ransom note.
  for word in note_dict:
    # if the word does not exists in the magazine or doesn't occurs sufficient
    # number of times, the note is not from this magazine page.
    if word not in magazine_dict or note_dict[word] > magazine_dict[word]:
      return False

  # if all the words in the note occurred in the magazine sufficient number
  # of times the note can be from the magazine page.
  return True

if __name__ == '__main__':
  note = r"""We have your daughter. If you care about her well being,
  you will do as we say. Do not inform the police or anyone else.
  Arrange 10 thousand rupees within 24 hours and wait for our call."""

  # Pardon the awkward english. I simply copied the ransom note's text and
  # edited it because I am lazy. :-)
  magazine = r"""We have the well being of your daughter as our first priority.
  If you too care about her and her pet dog's well being, this summer,
  you will do as we say. We suggest you to enroll them for our summer pet camp. Do not worry
  about the commute, we will take care of that and inform you about the
  details. We also police the pets with the help of our trained vets so that
  we don't need to bother you or anyone else. It will be fun for your daughter.
  Please arrange 10 thousand rupees as enrollment fee whose window closes
  within the next 24 hours and wait for our call."""

  print(is_ransom_source(note, magazine))
