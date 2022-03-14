"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    hash_table = set()
    hash_table.add(head)
    while head.next:
        if head in hash_table:
            return 1
        hash_table.add(head)
        head = head.next

    return 0
