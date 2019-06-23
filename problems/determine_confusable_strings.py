#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Given pairs of confusable chars, determine if two strings are confusables.
ex: (I, l), (c, e), (b, d), (g, q) etc.

Two characters are called confusables if they look similar to each other.

Two strings are considered confusable if they:
- are of equal length
- have confusable characters from a pair at the same posiiton in each string.

Usage:
$ python determine_confusbale_strings.py
"""
