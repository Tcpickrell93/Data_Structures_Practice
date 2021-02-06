import pytest

from dataStructs.singly_linked_list import (
        SinglyLinkedList, 
        Node 
)
from dataStructs.linked_list_exceptions import (
        LinkedListError,
        NodeIsNone,
        ListIsEmpty,
        NodeNotFound,
        InvalidPosition
)


@pytest.fixture
def new_list():
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
    a = new_list.head
    b = a.next
    c = b.next
    d = c.next
    yield (a, b, c, d)

@pytest.fixture
def empty_list():
    empty = SinglyLinkedList()
    yield empty

def test_insert_node_after_non_node(new_list, node_ref):
    with pytest.raises(NodeIsNone) as excinfo:
        new_list.insert_after(prev_node=None, data="z")
    assert excinfo.value.msg == "Previous node is None"
    assert excinfo.value.my_list == new_list

def test_delete_node_from_empty_list_by_key(empty_list):
    with pytest.raises(ListIsEmpty) as excinfo:
        empty_list.delete_by_key(key="a")
    assert excinfo.value.msg == "Cannot delete node from empty list"
    assert excinfo.value.my_list == empty_list

def test_delete_nonexistent_node_by_key(new_list, node_ref):
    with pytest.raises(NodeNotFound) as excinfo:
        new_list.delete_by_key(key="x")
    assert excinfo.value.msg == "Node with data='x' not found"
    assert excinfo.value.my_list == new_list

def test_delete_node_from_empty_list_by_position(empty_list):
    with pytest.raises(ListIsEmpty) as excinfo:
        empty_list.delete_by_pos(position=1)
    assert excinfo.value.msg == "Cannot delete node from empty list"
    assert excinfo.value.my_list == empty_list

def test_delete_nonexistent_node_by_position(new_list):
    with pytest.raises(NodeNotFound) as excinfo:
        new_list.delete_by_pos(position=8)
    assert excinfo.value.msg == "No node at position=8. List only has 4 nodes"
    
def test_delete_node_at_neg_position(new_list):
    with pytest.raises(InvalidPosition) as excinfo:
        new_list.delete_by_pos(position=-5)
    assert excinfo.value.msg == "Position must be a positive integer"
