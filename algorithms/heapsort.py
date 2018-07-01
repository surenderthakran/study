#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implements heapsort algorithm using Max Heaps.

The strategy is:
1. Max heapify the whole given array from root (index 0) to the last heap
   element (last element in array). This will put the largest element at the
   root.
2. Swap root element and the last heap element.
3. Reduce heap length by 1 by reducing the last heap element's position by 1.
4. Again max heapify the array from root to last heap element.
5. Repeat steps 2 to 4 until the heap length is 1 i.e. last heap element's
   position is 0.

Using Min heaps instead of max heap will be tricky. Like with max heaps, we
will increase the root's position after each min-heapify but unlike max heaps,
additionally we will need to take care of increasing the index of all the
elements otherwise the left and right child index calculations will break.

Usage:
$ python heapsort.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def sink_down(arr, index, last_index):
  """Sinks down an element in a max heap to its proper position.

  We need to sink down the element but not beyind the position of the last
  index.

  Args:
    index: (int) Index of the element we need to sink down.
    last_index: (int) Index of the last element in the heap.
  """
  while True:
    largest_index = index

    left_index = 2 * index + 1
    # If the left index is not beyond the last index and value at left index
    # is greater than the value at current largest index, set left as largest.
    if left_index <= last_index and arr[left_index] > arr[largest_index]:
      largest_index = left_index

    right_index = 2 * index + 2
    # If the right index is not beyond the last index and value at right index
    # is greater than the value at current largest index, set right as largest.
    if right_index < last_index and arr[right_index] > arr[largest_index]:
      largest_index = right_index

    # If the current index remains the largest that means the element is
    # already at its proper position so we exit.
    if largest_index == index:
      break

    # Swap the values at largest index and the current index.
    temp = arr[largest_index]
    arr[largest_index] = arr[index]
    arr[index] = temp

    # Set the new position of our element as the current index to further
    # attempt to sink it down.
    index = largest_index


def heapify(arr, last_index):
  """Heapifies the given array from root to the given last index.

  Args:
    arr: (list) List of integers to heapify.
    last_index: (int) Last index until which the array should be heaified.
  """
  # The last parent is the parent of the last element.
  last_parent_index = (last_index - 1) // 2
  # Return if the last parent is out of bounds.
  if last_parent_index < 0:
    return

  # Sink down all elements from the last parent up to the root.
  for parent_index in range(last_parent_index, -1, -1):
    # Sink down the parent but not below the last index position.
    sink_down(arr, parent_index, last_index)


def heapsort(arr):
  """Sorts a given array using heapsort technique.

  Args:
    arr: (list) List if integers to sort.

  Returns:
    List of sorted integers.
  """
  # Intial last index is the last element's position in the array.
  last_index = len(arr) - 1

  # Loop until the last index doesn't reaches the root.
  while last_index >= 0:
    # Heapify the array from root to the current last index.
    heapify(arr, last_index)

    # Swap root element with the value at the current last index.
    temp = arr[last_index]
    arr[last_index] = arr[0]
    arr[0] = temp

    # Move the last index position up by 1.
    last_index -= 1

  return arr


if __name__ == '__main__':
  assert heapsort([3, 4, 5, 6, 9, 1, 8, 2, 7, 0]) == (
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
