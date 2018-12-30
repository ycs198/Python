#!/bin/python

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node):
    while node:
        print node.data
        node = node.next


def insertNodeAtHead(head, data):
    newNode = SinglyLinkedListNode(data)
    if head is None:
        head = newNode
    else:
        newNode.next = head
        head = newNode
    return head

def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = SinglyLinkedListNode(data)
        current = head
    return head



if __name__ == '__main__':

    llist_count = int(raw_input())

    llist = SinglyLinkedList()

    for i in xrange(llist_count):
        llist_item = int(raw_input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head


    #print_singly_linked_list(llist.head)
