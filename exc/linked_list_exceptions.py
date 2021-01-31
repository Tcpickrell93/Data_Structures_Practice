class LinkedListError(Exception):
    """Basic exception for errors raised by singly linked lists"""
    pass

class NodeIsNone(LinkedListError):
    """Raised when node is expected but node is None"""
    def __init__(self, msg, my_list):
        self.msg = msg 
        self.my_list = my_list

class ListIsEmpty(LinkedListError):
    """Raised when list is expected but head is None"""
    def __init__(self, msg, my_list):
        self.msg = msg
        self.my_list = my_list

class NodeNotFound(LinkedListError):
    """Raised when node is not found in list by key"""
    def __init__(self, msg, my_list):
        self.msg = msg
        self.my_list = my_list

