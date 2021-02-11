"""Contains class for stack and class for nodes within lists"""

from .linked_list_exceptions import(
        NodeIsNone,
        ListIsEmpty,
        NodeNotFound,
        InvalidPosition,
        SameNode
)
from .nodes import SLLNode as Node

class Stack:
    """Class for implementing Stack data structure"""
    def __init__(self):
        self.head = None

    def push(self, data):
        """Create new node from data and add to beginning of list"""
        # Create new node with provided data
        new_node = Node(data)

        # Update "next" of new node
        new_node.next = self.head

        # Set new node to head
        self.head = new_node

    def pop(self):
        """Remove head node and return it"""
        # Save popped node in temp variable
        popped = self.head

        # Change head node
        self.head = self.head.next

        return popped

    def isEmpty():
        """Return boolean for whether stack is empty"""
        if self.head is None:
            return True
        else:
            return False

    def peek():
        """Return top Node in stack without removing it"""
        return self.head

