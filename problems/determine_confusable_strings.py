#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Determine if two given strings are confusables.

Two characters are called confusables if they look similar to each other.
ex: (I, l), (c, e), (b, d), (g, q) etc.

Two strings are considered confusable if they:
- are of equal length
- have confusable characters from a pair at the same posiiton in each string.

Usage:
$ python determine_confusbale_strings.py
"""
