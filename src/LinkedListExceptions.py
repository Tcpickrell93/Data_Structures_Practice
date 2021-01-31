class SinglyLinkedListError(Exception):
    """Basic exception for errors raised by singly linked lists"""
    pass

class NodeIsNone(SinglyLinkedListError):
    """Raised when node is expected but node is None"""
    def __init__(self, msg, my_list, new_node):
        self.msg = msg 
        self.my_list = my_list
        self.new_node = new_node

class ListIsEmpty(SinglyLinkedListError):
    """Raised when list is expected but head is None"""
    def __init__(self, msg, my_list):
        self.msg = msg
        self.my_list = my_list


