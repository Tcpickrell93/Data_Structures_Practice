"""Contains tests for positive functionality in singly_linked_list"""

import pytest
from dataStructs.singly_linked_list import SinglyLinkedList, Node


@pytest.fixture
def new_list():
    """Creates simple singly-linked list for each test to use"""
    letters = SinglyLinkedList()
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
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
    empty = SinglyLinkedList()
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

def test_count_list(new_list):
    assert new_list.get_count() == 4

def test_push_node_to_front(new_list, node_ref):
    new_list.push(data="z")
    node_1 = new_list.head
    node_2 = node_1.next
    assert new_list.get_count() == 5
    assert node_1.data == "z"
    assert node_2 is node_ref[0]

def test_push_node_to_front_of_empty_list(empty_list):
    empty_list.push(data="a")
    assert empty_list.head.data == "a"
    assert empty_list.head.next is None

def test_insert_after_node_at_middle(new_list, node_ref):
    new_list.insert_after(prev_node=new_list.head, data="z")
    node_1 = new_list.head
    node_2 = node_1.next
    node_3 = node_2.next
    assert new_list.get_count() == 5
    assert node_1 is node_ref[0]
    assert node_2.data == "z"
    assert node_3 is node_ref[1]

def test_insert_after_node_at_end(new_list, node_ref):
    new_list.insert_after(prev_node=node_ref[3], data="z")
    node_4 = node_ref[3]
    assert new_list.get_count() == 5
    assert node_4.next.data == "z"

def test_append_node_to_end(new_list, node_ref):
    new_list.append(data="z")
    node_4 = node_ref[3]
    assert new_list.get_count() == 5
    assert node_4.next.data == "z"

def test_append_node_to_empty_list(empty_list):
    empty_list.append(data="a")
    assert empty_list.head.data == "a"

def test_delete_head_by_key(new_list, node_ref):
    new_list.delete_by_key(key="a")
    assert new_list.get_count() == 3
    assert new_list.head is node_ref[1]

def test_delete_middle_node_by_key(new_list, node_ref):
    new_list.delete_by_key(key="b")
    assert new_list.get_count() == 3
    assert new_list.head is node_ref[0]
    assert new_list.head.next is node_ref[2]

def test_delete_last_node_by_key(new_list, node_ref):
    new_list.delete_by_key(key="d")
    node_3 = node_ref[2]
    assert new_list.get_count() == 3
    assert node_3.next is None

def test_delete_head_by_position(new_list, node_ref):
    new_list.delete_by_pos(position=0)
    assert new_list.get_count() == 3
    assert new_list.head is node_ref[1]

def test_delete_middle_node_by_position(new_list, node_ref):
    new_list.delete_by_pos(position=1)
    assert new_list.get_count() == 3
    assert new_list.head.next is node_ref[2]

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

def test_swap_adjacent_nodes_key_1_as_head(new_list, node_ref):
    new_list.swap_nodes(key_1="a", key_2="b")
    assert new_list.head is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is node_ref[2]
    assert node_ref[2].next is node_ref[3]
    assert node_ref[3].next is None

def test_swap_nonadjacent_nodes_key_2_as_head(new_list, node_ref):
    new_list.swap_nodes(key_1="c", key_2="a")
    assert new_list.head is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is node_ref[3]
    assert node_ref[3].next is None

def test_swap_adjacent_nodes_key_2_as_head(new_list, node_ref):
    new_list.swap_nodes(key_1="b", key_2="a")
    assert new_list.head is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is node_ref[2]
    assert node_ref[2].next is node_ref[3]
    assert node_ref[3].next is None

def test_swap_nonadjacent_nodes_key_1_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="d", key_2="b")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is None

def test_swap_adjacent_nodes_key_1_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="d", key_2="c")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[1]
    assert node_ref[1].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is None

def test_swap_nonadjacent_nodes_key_2_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="b", key_2="d")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is None

def test_swap_adjacent_nodes_key_2_as_last_node(new_list, node_ref):
    new_list.swap_nodes(key_1="c", key_2="d")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[1]
    assert node_ref[1].next is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is None

def test_swap_middle_nodes_with_keys_adjacent(new_list, node_ref):
    new_list.swap_nodes(key_1="b", key_2="c")
    assert new_list.head is node_ref[0]
    assert node_ref[0].next is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is node_ref[3]
    assert node_ref[3].next is None

def test_reverse_list(new_list, node_ref):
    new_list.reverse_list()
    assert new_list.head is node_ref[3]
    assert node_ref[3].next is node_ref[2]
    assert node_ref[2].next is node_ref[1]
    assert node_ref[1].next is node_ref[0]
    assert node_ref[0].next is None
