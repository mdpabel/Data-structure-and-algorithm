#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#


#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
"""
Head->1<->2<->3<->5->Null
4
prev.next = 4
node.prev = prev
node.next = current
current.prev = node

2 3 4
"""


def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)
    current_node = llist
    prev_node = llist

    if llist is None:
        return new_node

    if current_node.data > data:
        current_node.prev = new_node
        new_node.next = current_node
        return new_node

    while current_node is not None and current_node.data < data:
        prev_node = current_node
        current_node = current_node.next

    if current_node is None:
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = None
        return llist

    prev_node.next = new_node
    new_node.prev = prev_node
    new_node.next = current_node
    current_node.prev = new_node

    return llist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
