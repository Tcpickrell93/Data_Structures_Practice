"""Contains classes for different types of nodes"""


class SLLNode:
    """Singly-Linked List Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class DLLNode:
    """Doubly-Linked List Node"""
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
