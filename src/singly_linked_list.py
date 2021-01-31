from src.linked_list_exceptions import(
        LinkedListError,
        NodeIsNone,
        ListIsEmpty,
        NodeNotFound
)

class Node:
    """Node for Singly-Linked List"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Singly-Linked List"""
    def __init__(self):
        self.head = None

    def push(self, data):
        # Create new node with provided data
        new_node = Node(data)

        # Update "next" of new node
        new_node.next = self.head

        # Set new node to head
        self.head = new_node

    def insert_after(self, prev_node, data):
        # Create new node with provided data
        new_node = Node(data)

        # Set "next" of new node to be the "next" of the previous node
        try:
            new_node.next = prev_node.next
        except AttributeError:
            raise NodeIsNone(msg="Previous node is None", 
                             my_list=self,
                             new_node=new_node)

        # Set "next" of previous node to be new node
        prev_node.next = new_node

    def append(self, data):
        # Create new node with provided data
        new_node = Node(data)

        # Check to see if list exists
        if self.head is None:
            self.head = new_node        # Start new list
            return

        # Traverse through list until last node reached
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next

        # Set new node to "next" of last node in list
        temp_node.next = new_node

    def delete_by_key(self, key):
        # Check to see if list is empty
        if self.head is None:
            raise ListIsEmpty(msg="Cannot delete node from empty list",
                              my_list=self)

        # Check to see if key is head node
        temp_node = self.head
        if temp_node.data == key:
            self.head = temp_node.next      # Change head node before deleting
            return

        # Find node equal to key
        while temp_node:
            if temp_node.data == key:
                break
            prev_node = temp_node
            temp_node = temp_node.next

        # Check to see if key was found in list
        if not temp_node:
            raise NodeNotFound(msg=f"Node with data='{key}' not found",
                               my_list=self)

        # Link previous node to next node
        prev_node.next = temp_node.next

    def delete_by_pos(self, position):
        # Check to see if list is empty
        if self.head is None:
            return

        # Check to see if position is head node
        temp_node = self.head
        if position == 0:
            temp_node.head = temp_node.next      # Change head node before deleting
            return

        # Traverse through list to desired position
        for i in range(position):
            if temp_node.next:
                prev_node = temp_node
                temp_node = temp_node.next
            else:
                return

        # Link previous node to next node
        prev_node.next = temp_node.next

    def swap_nodes(self, key_1, key_2):
        # Check if keys are the same
        if key_1 == key_2:
            return

        # Find key_1 node
        prev_1 = None
        temp_1 = self.head
        while temp_1 and temp_1.data != key_1:
            prev_1 = temp_1
            temp_1 = temp_1.next

        # Find key_2 node
        prev_2 = None
        temp_2 = self.head
        while temp_2 and temp_2.data != key_2:
            prev_2 = temp_2
            temp_2 = temp_2.next

        # Can't swap if one of them does not exist in list
        if temp_1 is None or temp_2 is None:
            return

        # Check if key_1 is head
        if prev_1:
            prev_1.next = temp_2
        else:
            self.head = temp_2

        # Check if key_2 is head
        if prev_2:
            prev_2.next = temp_1
        else:
            self.head = temp_1

        # Swap next nodes
        temp_3 = temp_1.next
        temp_1.next = temp_2.next
        temp_2.next = temp_3

    def reverse_list(self):
        cur_node = self.head
        prev_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next

    def generate_list(self):
        temp_node = self.head
        while temp_node:
            yield temp_node.data
            temp_node = temp_node.next

    def get_count(self):
        count = 0
        temp_node = self.head
        while temp_node:
            count += 1
            temp_node = temp_node.next
        return count
