"""Contains tests for positive functionality in doubly_linked_list"""

import pytest
from dataStructs.doubly_linked_list import Node, DoublyLinkedList

@pytest.fixture
def new_list():
    """Creates simple singly-linked list for each test to use"""
    letters = DoublyLinkedList()
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    d.prev = c
    c.prev = b
    b.prev = a
    letters.head = a
    yield letters

@pytest.fixture
def node_ref(new_list):
    """Used as reference for objects' initial positions in list"""
    a = new_list.head
    b = a.next
    c = b.next
    d = c.next
    yield (a, b, c, d)

@pytest.fixture
def empty_list():
    """Creates an empty singly-linked list"""
    empty = DoublyLinkedList()
    yield empty

def test_list(new_list, node_ref):
    node_1 = new_list.head
    node_2 = node_1.next
    node_3 = node_2.next
    node_4 = node_3.next
    assert node_1.data == "a"
    assert node_2.data == "b"
    assert node_3.data == "c"
    assert node_4.data == "d"
    assert node_1 is node_ref[0]
    assert node_2 is node_ref[1]
    assert node_3 is node_ref[2]
    assert node_4 is node_ref[3]
    assert node_4.prev is node_3
    assert node_3.prev is node_2
    assert node_2.prev is node_1
    assert node_1.prev is None
    
def test_count_list(new_list):
    assert new_list.get_count() == 4

def test_push_node_to_front(new_list, node_ref):
    new_list.push(data="z")
    node_1 = new_list.head
    node_2 = node_1.next
    assert new_list.get_count() == 5
    assert node_1.data == "z"
    assert node_2 is node_ref[0]
    assert node_2.prev is node_1

def test_push_node_to_front_of_empty_list(empty_list):
    empty_list.push(data="a")
    assert empty_list.head.data == "a"
    assert empty_list.head.next is None
    assert empty_list.head.prev is None

def test_insert_after_node_at_middle(new_list, node_ref):
    new_list.insert_after(prev_node=new_list.head, data="z")
    node_1 = new_list.head
    node_2 = node_1.next
    node_3 = node_2.next
    assert new_list.get_count() == 5
    assert node_1 is node_ref[0]
    assert node_2.data == "z"
    assert node_2.prev is node_1 
    assert node_3 is node_ref[1]
    assert node_3.prev is node_2 

def test_insert_after_node_at_end(new_list, node_ref):
    new_list.insert_after(prev_node=node_ref[3], data="z")
    node_4 = node_ref[3]
    node_5 = node_4.next
    assert new_list.get_count() == 5
    assert node_5.data == "z"
    assert node_5.prev is node_4

def test_append_node_to_end(new_list, node_ref):
    new_list.append(data="z")
    node_4 = node_ref[3]
    node_5 = node_4.next
    assert new_list.get_count() == 5
    assert node_5.data == "z"
    assert node_5.prev is node_4

def test_append_node_to_empty_list(empty_list):
    empty_list.append(data="a")
    assert empty_list.head.data == "a"
    assert empty_list.head.next is None
    assert empty_list.head.prev is None

def test_delete_head_by_key(new_list, node_ref):
    new_list.delete_by_key(key="a")
    assert new_list.get_count() == 3
    assert new_list.head is node_ref[1]
    assert new_list.head.prev is None

def test_delete_middle_node_by_key(new_list, node_ref):
    new_list.delete_by_key(key="b")
    node_2 = new_list.head.next
    assert new_list.get_count() == 3
    assert new_list.head is node_ref[0]
    assert node_2 is node_ref[2]
    assert node_2.prev is node_ref[0]

def test_delete_last_node_by_key(new_list, node_ref):
    new_list.delete_by_key(key="d")
    node_3 = node_ref[2]
    assert new_list.get_count() == 3
    assert node_3.next is None

def test_delete_head_by_position(new_list, node_ref):
    new_list.delete_by_pos(position=0)
    assert new_list.get_count() == 3
    assert new_list.head is node_ref[1]
    assert node_ref[1].prev is None

def test_delete_middle_node_by_position(new_list, node_ref):
    new_list.delete_by_pos(position=1)
    node_2 = new_list.head.next
    assert new_list.get_count() == 3
    assert node_2 is node_ref[2]
    assert node_2.prev is new_list.head

def test_delete_last_node_by_position(new_list, node_ref):
    new_list.delete_by_pos(position=3)
    assert new_list.get_count() == 3
    assert node_ref[2].next is None

def test_swap_nonadjacent_nodes_key_1_as_head(new_list, node_ref):
    new_list.swap_nodes(key_1="a", key_2="c")
    assert new_list.head is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is node_ref[3]
    assert node_ref[3].next is None
    assert node_ref[1].prev is node_ref[2]
    assert node_ref[0].prev is node_ref[1]
    assert node_ref[3].prev is node_ref[0]

def test_swap_adjacent_nodes_key_1_as_head(new_list, node_ref):
    new_list.swap_nodes(key_1="a", key_2="b")
    assert new_list.head is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is node_ref[2]
    assert node_ref[2].next is node_ref[3]
    assert node_ref[3].next is None
    assert node_ref[0].prev is node_ref[1]
    assert node_ref[2].prev is node_ref[0]
    assert node_ref[3].prev is node_ref[2]

def test_swap_nonadjacent_nodes_key_2_as_head(new_list, node_ref):
    new_list.swap_nodes(key_1="c", key_2="a")
    assert new_list.head is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is node_ref[3]
    assert node_ref[3].next is None
    assert node_ref[1].prev is node_ref[2]
    assert node_ref[0].prev is node_ref[1]
    assert node_ref[3].prev is node_ref[0]

def test_swap_adjacent_nodes_key_2_as_head(new_list, node_ref):
    new_list.swap_nodes(key_1="b", key_2="a")
    assert new_list.head is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is node_ref[2]
    assert node_ref[2].next is node_ref[3]
    assert node_ref[3].next is None
    assert node_ref[0].prev is node_ref[1]
    assert node_ref[2].prev is node_ref[0]
    assert node_ref[3].prev is node_ref[2]

def test_swap_nonadjacent_nodes_key_1_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="d", key_2="b")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is None
    assert node_ref[3].prev is node_ref[0]
    assert node_ref[2].prev is node_ref[3]
    assert node_ref[1].prev is node_ref[2]

def test_swap_adjacent_nodes_key_1_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="d", key_2="c")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[1]
    assert node_ref[1].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is None
    assert node_ref[1].prev is node_ref[0]
    assert node_ref[3].prev is node_ref[1]
    assert node_ref[2].prev is node_ref[3]

def test_swap_nonadjacent_nodes_key_2_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="b", key_2="d")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is None
    assert node_ref[3].prev is node_ref[0]
    assert node_ref[2].prev is node_ref[3]
    assert node_ref[1].prev is node_ref[2]

def test_swap_adjacent_nodes_key_2_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="c", key_2="d")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[1]
    assert node_ref[1].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is None
    assert node_ref[1].prev is node_ref[0]
    assert node_ref[3].prev is node_ref[1]
    assert node_ref[2].prev is node_ref[3]
"""
    def test_delete_head_by_key(self):
        my_log.log.debug("test_delete_head_by_key")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_key(key="Monday")
        self.assertIs(week.head, self.day_2)
        self.assertIs(week.head.prev, None)

        my_log.log.debug("Delete Monday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_delete_middle_node_by_key(self):
        my_log.log.debug("test_delete_middle_node_by_key")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_key(key="Tuesday")
        self.assertIs(week.head.next, self.day_3)
        self.assertIs(self.day_3.prev, week.head)

        my_log.log.debug("Delete Tuesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_delete_last_node_by_key(self):
        my_log.log.debug("test_delete_last_node_by_key")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_key(key="Sunday")
        self.assertIs(self.day_6.next, None)

        my_log.log.debug("Delete Sunday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_delete_nonexistent_node_by_key(self):
        my_log.log.debug("test_delete_nonexistent_key")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_key(key="Yesterday")

        my_log.log.debug("Delete Yesterday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_delete_head_by_position(self):
        my_log.log.debug("test_delete_head_by_position")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_pos(position=0)
        self.assertIs(week.head, self.day_2)
        self.assertIs(week.head.prev, None)

        my_log.log.debug("Delete Monday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_delete_middle_node_by_position(self):
        my_log.log.debug("test_delete_middle_node_by_position")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_pos(position=1)
        self.assertIs(week.head.next, self.day_3)
        self.assertIs(week.head, self.day_3.prev)

        my_log.log.debug("Delete Tuesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_delete_last_node_by_position(self):
        my_log.log.debug("test_delete_last_node_by_position")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_pos(position=6)
        self.assertIs(self.day_6.next, None)

        my_log.log.debug("Delete Sunday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_delete_nonexistent_node_by_position(self):
        my_log.log.debug("test_delete_nonexistent_key")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.delete_by_pos(position=7)

        my_log.log.debug("Delete position 7")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_nonadjacent_nodes_key_1_as_head(self):
        my_log.log.debug("test_swap_nonadjacent_nodes_key_1_as_head")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Monday", key_2="Wednesday")
        second = week.head.next
        third = second.next
        # Test head and links relating to head
        self.assertIs(week.head, self.day_3)
        self.assertIs(week.head, self.day_2.prev)
        self.assertIs(week.head.prev, None)
        self.assertIs(week.head.next, self.day_2)
        # Test third and links relating to third
        self.assertIs(third, self.day_1)
        self.assertIs(third, self.day_2.next)
        self.assertIs(third, self.day_4.prev)
        self.assertIs(third.next, self.day_4)
        self.assertIs(third.prev, self.day_2)

        my_log.log.debug("Swap Monday and Wednesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_adjacent_nodes_key_1_as_head(self):
        my_log.log.debug("test_swap_adjacent_nodes_key_1_as_head")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Monday", key_2="Tuesday")
        second = week.head.next
        # Test head and links relating to head
        self.assertIs(week.head, self.day_2)
        self.assertIs(week.head, self.day_1.prev)
        self.assertIs(week.head.prev, None)
        self.assertIs(week.head.next, self.day_1)
        # Test second and links relating to second
        self.assertIs(second, self.day_1)
        self.assertIs(second, self.day_2.next)
        self.assertIs(second, self.day_3.prev)
        self.assertIs(second.next, self.day_3)
        self.assertIs(second.prev, self.day_2)

        my_log.log.debug("Swap Monday and Tuesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_nonadjacent_nodes_key_2_as_head(self):
        my_log.log.debug("test_swap_nonadjacent_nodes_key_2_as_head")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Thursday", key_2="Monday")
        second = week.head.next
        third = second.next
        fourth = third.next
        # Test head and links relating to head
        self.assertIs(week.head, self.day_4)
        self.assertIs(week.head, self.day_2.prev)
        self.assertIs(week.head.prev, None)
        self.assertIs(week.head.next, self.day_2)
        # Test fourth and links relating to fourth
        self.assertIs(fourth, self.day_1)
        self.assertIs(fourth, self.day_3.next)
        self.assertIs(fourth, self.day_5.prev)
        self.assertIs(fourth.next, self.day_5)
        self.assertIs(fourth.prev, self.day_3)

        my_log.log.debug("Swap Monday and Thursday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_adjacent_nodes_key_2_as_head(self):
        my_log.log.debug("test_swap_adjacent_nodes_key_2_as_head")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Tuesday", key_2="Monday")
        second = week.head.next
        # Test head and links relating to head
        self.assertIs(week.head, self.day_2)
        self.assertIs(week.head, self.day_1.prev)
        self.assertIs(week.head.prev, None)
        self.assertIs(week.head.next, self.day_1)
        # Test second and links relating to second
        self.assertIs(second, self.day_1)
        self.assertIs(second, self.day_2.next)
        self.assertIs(second, self.day_3.prev)
        self.assertIs(second.next, self.day_3)
        self.assertIs(second.prev, self.day_2)

        my_log.log.debug("Swap Monday and Tuesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_nodes_key_1_nonexistent(self):
        my_log.log.debug("test_swap_nodes_key_1_nonexistent")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Yesterday", key_2="Wednesday")

        my_log.log.debug("Swap Yesterday and Wednesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_nodes_key_2_nonexistent(self):
        my_log.log.debug("test_swap_nodes_key_2_nonexistent")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Monday", key_2="Yesterday")

        my_log.log.debug("Swap Yesterday and Monday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_nonadjacent_nodes_key_1_as_last_node(self):
        my_log.log.debug("test_swap_nonadjacent_nodes_key_1_as_last_node")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Sunday", key_2="Wednesday")
        second = week.head.next
        third = second.next
        fourth = third.next
        fifth = fourth.next
        sixth = fifth.next
        seventh = sixth.next
        # Test third and links relating to third
        self.assertIs(third, self.day_7)
        self.assertIs(third, self.day_2.next)
        self.assertIs(third, self.day_4.prev)
        self.assertIs(third.next, self.day_4)
        self.assertIs(third.prev, self.day_2)
        # Test seventh and links relating to seventh
        self.assertIs(seventh, self.day_3)
        self.assertIs(seventh, self.day_6.next)
        self.assertIs(seventh.next, None)
        self.assertIs(seventh.prev, self.day_6)

        my_log.log.debug("Swap Wednesday and Sunday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_adjacent_nodes_key_1_as_last_node(self):
        my_log.log.debug("test_swap_adjacent_nodes_key_1_as_last_node")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Sunday", key_2="Saturday")
        second = week.head.next
        third = second.next
        fourth = third.next
        fifth = fourth.next
        sixth = fifth.next
        seventh = sixth.next
        # Test sixth and links relating to sixth
        self.assertIs(sixth, self.day_7)
        self.assertIs(sixth, self.day_5.next)
        self.assertIs(sixth, self.day_6.prev)
        self.assertIs(sixth.next, self.day_6)
        self.assertIs(sixth.prev, self.day_5)
        # Test seventh and links relating to seventh
        self.assertIs(seventh, self.day_6)
        self.assertIs(seventh, self.day_7.next)
        self.assertIs(seventh.next, None)
        self.assertIs(seventh.prev, self.day_7)

        my_log.log.debug("Swap Saturday and Sunday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_nonadjacent_nodes_key_2_as_last_node(self):
        my_log.log.debug("test_swap_nonadjacent_nodes_key_2_as_last_node")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Tuesday", key_2="Sunday")
        second = week.head.next
        third = second.next
        fourth = third.next
        fifth = fourth.next
        sixth = fifth.next
        seventh = sixth.next
        # Test second and links relating to second
        self.assertIs(second, self.day_7)
        self.assertIs(second, self.day_1.next)
        self.assertIs(second, self.day_3.prev)
        self.assertIs(second.next, self.day_3)
        self.assertIs(second.prev, self.day_1)
        # Test seventh and links relating to seventh
        self.assertIs(seventh, self.day_2)
        self.assertIs(seventh, self.day_6.next)
        self.assertIs(seventh.next, None)
        self.assertIs(seventh.prev, self.day_6)

        my_log.log.debug("Swap Tuesday and Sunday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_adjacent_nodes_key_2_as_last_node(self):
        my_log.log.debug("test_swap_adjacent_nodes_key_2_as_last_node")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Saturday", key_2="Sunday")
        second = week.head.next
        third = second.next
        fourth = third.next
        fifth = fourth.next
        sixth = fifth.next
        seventh = sixth.next
        # Test second and links relating to second
        self.assertIs(sixth, self.day_7)
        self.assertIs(sixth, self.day_5.next)
        self.assertIs(sixth, self.day_6.prev)
        self.assertIs(sixth.next, self.day_6)
        self.assertIs(sixth.prev, self.day_5)
        # Test seventh and links relating to seventh
        self.assertIs(seventh, self.day_6)
        self.assertIs(seventh, self.day_7.next)
        self.assertIs(seventh.next, None)
        self.assertIs(seventh.prev, self.day_7)

        my_log.log.debug("Swap Saturday and Sunday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_middle_nodes_with_keys_adjacent(self):
        my_log.log.debug("test_swap_middle_nodes_with_keys_adjacent")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Tuesday", key_2="Wednesday")
        second = week.head.next
        third = second.next
        fourth = third.next
        # Test second and links relating to second
        self.assertIs(second, self.day_3)
        self.assertIs(second, self.day_1.next)
        self.assertIs(second, self.day_2.prev)
        self.assertIs(second.next, self.day_2)
        self.assertIs(second.prev, self.day_1)
        # Test third and links relating to third
        self.assertIs(third, self.day_2)
        self.assertIs(third, self.day_3.next)
        self.assertIs(third, self.day_4.prev)
        self.assertIs(third.next, self.day_4)
        self.assertIs(third.prev, self.day_3)

        my_log.log.debug("Swap Tuesday and Wednesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_swap_middle_nodes_with_keys_nonadjacent(self):
        my_log.log.debug("test_swap_middle_nodes_with_keys_nonadjacent")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.swap_nodes(key_1="Tuesday", key_2="Thursday")
        second = week.head.next
        third = second.next
        fourth = third.next
        # Test second and links relating to second
        self.assertIs(second, self.day_4)
        self.assertIs(second, self.day_1.next)
        self.assertIs(second, self.day_3.prev)
        self.assertIs(second.next, self.day_3)
        self.assertIs(second.prev, self.day_1)
        # Test fourth and links relating to fourth
        self.assertIs(fourth, self.day_2)
        self.assertIs(fourth, self.day_3.next)
        self.assertIs(fourth, self.day_5.prev)
        self.assertIs(fourth.next, self.day_5)
        self.assertIs(fourth.prev, self.day_3)

        my_log.log.debug("Swap Tuesday and Thursday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_reverse_list(self):
        my_log.log.debug("test_reverse_list")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.reverse_list()
        second = week.head.next
        third = second.next
        fourth = third.next
        fifth = fourth.next
        sixth = fifth.next
        seventh = sixth.next
        self.assertIs(week.head, self.day_7)
        self.assertIs(week.head.prev, None)
        self.assertIs(second, self.day_6)
        self.assertIs(second.prev, self.day_7)
        self.assertIs(third, self.day_5)
        self.assertIs(third.prev, self.day_6)
        self.assertIs(fourth, self.day_4)
        self.assertIs(fourth.prev, self.day_5)
        self.assertIs(fifth, self.day_3)
        self.assertIs(fifth.prev, self.day_4)
        self.assertIs(sixth, self.day_2)
        self.assertIs(sixth.prev, self.day_3)
        self.assertIs(seventh, self.day_1)
        self.assertIs(seventh.prev, self.day_2)
        self.assertIs(seventh.next, None)

        my_log.log.debug("Reverse Week")
        for node in week.generate_list():
            my_log.log.debug(node)
"""
