#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""Implement an algorithm to find the starting node in a circular linked list.

Circular linked lists need not circle back to the node at the head. The last
node in a circular linked list can point to any node in the list. We need to
find that particular node in the system which is referenced by two nodes.

Two understand the solution we first need to understand a scenario. Imagine a
circle with circumference n. Two players p1 and p2 starting running along the
circle in the same direction where p1 runs twice as fats as p2.The two players
will meet again at the starting point itself.

Now imagine that the faster player p1 has a head start of k. This time the two
players will meet again at a point k units before the starting point.
Imagine the two players met at a point l units before the start, at this point
in time the distance travelled by p2 would be (n - l) while the distance
travelled by p1 would be (n + n - (K + l)). Since p1 runs twice as fast as p2,
2(n - l) = 2n - (K + l).
Solving this given us l = k.

We use the same scenario to find a solution to our problem.

Consider two pointers p1 and p2 pointing to the first element of the linked
list. Again, p1 traverses twice as fast as p2. When p2 enters the first node of
the circular portion of the list, consider p1 to be k nodes ahead. Also the
distance of p2 from the head of the list will be k and p1's distance will be
2k.
We continue moving both the points forward until they meet again and as we
saw earlier, they will meet again k nodes before the starting node of the
circle. Here we point p1 to the head of the list and at this point both p1 and
p2 are k distance away from the starting node of the circle. We again start
moving both the points ahead but this time at equal speed. The node at which
both the points meet is the starting point of the circle.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
  """Implements a node in a circular linked list."""

  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return repr(self.data)

  def get_next(self):
    """Returns the next node to the current node."""
    if self.next:
      return self.next

    return None

  def get_second_next(self):
    """Returns the next to next node of the current node."""
    if self.next and self.next.next:
      return self.next.next

    return None


class CircularLinkedList(object):
  """Implements a circular single linked list."""

  def __init__(self):
    self.head = None

  def add(self, node):
    self.head = node

  def append(self, node_1, node_2):
    node_1.next = node_2

  def get_starting_node(self):
    """Returns the value of the starting node in a circular linked list."""
    # Point p1 and p2 to the first node in the list.
    p1 = self.head
    p2 = self.head

    # Move p1 two nodes forward.
    p1 = p1.get_second_next()
    # Move p2 one node forward.
    p2 = p2.get_next()

    # Keep moving both points forward until they meet again.
    while id(p1) != id(p2):
      p1 = p1.get_second_next()
      p2 = p2.get_next()

    # The the two points have met, point p1 again to the first node.
    p1 = self.head

    # Keep moving both points forward at equal speed until they meet.
    while id(p1) != id(p2):
      p1 = p1.get_next()
      p2 = p2.get_next()

    # Return the node at which the two points met.
    return p1.data


def create_circular_linked_list():
  """Creates a circular linked list."""
  linked_list = CircularLinkedList()
  node_1 = Node(1)
  linked_list.add(node_1)

  node_2 = Node(2)
  linked_list.append(node_1, node_2)

  node_3 = Node(3)
  linked_list.append(node_2, node_3)

  node_4 = Node(4)
  linked_list.append(node_3, node_4)

  node_5 = Node(5)
  linked_list.append(node_4, node_5)

  node_6 = Node(6)
  linked_list.append(node_5, node_6)

  node_7 = Node(7)
  linked_list.append(node_6, node_7)

  node_8 = Node(8)
  linked_list.append(node_7, node_8)

  node_9 = Node(9)
  linked_list.append(node_8, node_9)

  linked_list.append(node_9, node_4)

  return linked_list


if __name__ == '__main__':
  circular_list = create_circular_linked_list()

  assert circular_list.get_starting_node() == 4
