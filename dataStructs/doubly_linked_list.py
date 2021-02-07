"""Contains class for singly-linked lists and class for nodes within lists"""

from .linked_list_exceptions import(
        NodeIsNone,
        ListIsEmpty,
        NodeNotFound,
        InvalidPosition,
        SameNode
)

class Node:
    """Doubly-Linked List Node"""
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """Doubly-Linked List"""
    def __init__(self):
        self.head = None

    def push(self, data):
        """Create new node from data and add to beginning of list"""
        # Create new node with provided data
        new_node = Node(data)

        # Update "next" of new node
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        # Set new node to head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """Create new node from data and add after provided node"""
        # Check if prev_node exists
        if prev_node is None:
            return

        # Create new node with provided data
        new_node = Node(data)

        # Change links between nodes
        next_node = prev_node.next
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        if next_node:
            next_node.prev = new_node

    def append(self, data):
        """Create new node from data and add to end of list"""
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

        # Update links
        temp_node.next = new_node
        new_node.prev = temp_node

    def delete_by_key(self, key):
        """Delete node from list where key matches the value stored in data"""
        # Check to see if list is empty
        if self.head is None:
            return

        # Check to see if key is head node
        temp_node = self.head
        if temp_node.data == key:
            self.head = temp_node.next
            self.head.prev = None
            return

        # Find node equal to key
        while temp_node:
            if temp_node.data == key:
                break
            prev_node = temp_node
            temp_node = temp_node.next

        # Check to see if key was found in list
        if not temp_node:
            return

        # Link previous node to next node
        if temp_node.next:
            next_node = temp_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            prev_node.next = None

    def delete_by_pos(self, position):
        """Delete Node by postion within list"""
        # Check to see if list is empty
        if self.head is None:
            return

        # Check to see if position is head node
        temp_node = self.head
        if position == 0:
            self.head = temp_node.next
            self.head.prev = None
            return

        # Traverse through list to desired position
        for i in range(position):
            if temp_node.next:
                prev_node = temp_node
                temp_node = temp_node.next
            else:
                return

        # Link previous node to next node
        if temp_node.next:
            next_node = temp_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            prev_node.next = None

    def swap_nodes(self, key_1, key_2):
        """Swap two nodes in list identified by provided key values"""
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

        # Save next nodes to update links
        next_1 = temp_1.next
        next_2 = temp_2.next

        # Check if key_1 is head or adjacent to key_2
        if prev_1 is None:
            # Temp_1 is currently head
            self.head = temp_2
            self.head.prev = None
        elif prev_1 is not temp_2:
            # Nodes are not adjacent with temp_2 before temp_1
            prev_1.next = temp_2
            temp_2.prev = prev_1
        elif prev_1 is temp_2:
            # Nodes are adjacent
            temp_1.next = temp_2
            temp_2.prev = temp_1
            temp_2.next = next_1
            if next_1:
                next_1.prev = temp_2

        # Check if key_2 is head or adjacent to key_1
        if prev_2 is None:
            # Temp_2 is currently head
            self.head = temp_1
            self.head.prev = None
        elif prev_2 is not temp_1:
            # Nodes are not adjacent with temp_2 before temp_1
            prev_2.next = temp_1
            temp_1.prev = prev_2
        elif prev_2 is temp_1:
            # Nodes are adjacent
            temp_2.next = temp_1
            temp_1.prev = temp_2
            temp_1.next = next_2
            if next_2:
                next_2.prev = temp_1

        # Swap next nodes if not adjacent
        if prev_2 is not temp_1 and prev_1 is not temp_2:
            temp_1.next = next_2
            temp_2.next = next_1
            if next_1:
                next_1.prev = temp_2
            if next_2:
                next_2.prev = temp_1

    def reverse_list(self):
        """Reverse order of the list"""
        cur_node = self.head
        prev_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            cur_node.prev = next_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def generate_list(self):
        """Generator function to yield nodes from list"""
        temp_node = self.head
        while temp_node:
            if not temp_node.next:
                last_node = temp_node
            yield temp_node.data
            temp_node = temp_node.next

        temp_node = last_node
        while temp_node:
            yield temp_node.data
            temp_node = temp_node.prev

    def get_count(self):
        """Return number of nodes in list"""
        count = 0
        temp_node = self.head
        while temp_node:
            count += 1
            temp_node = temp_node.next
        return count
