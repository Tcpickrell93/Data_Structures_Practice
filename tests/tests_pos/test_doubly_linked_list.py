"""
import unittest
import logging

import logger
from Doubly_Linked_List import Node, DoublyLinkedList

my_log = logger.Logger(name=__name__, level=logging.DEBUG)


class TestDLL(unittest.TestCase):
    def setUp(self):
        self.day_1 = Node("Monday")
        self.day_2 = Node("Tuesday")
        self.day_3 = Node("Wednesday")
        self.day_4 = Node("Thursday")
        self.day_5 = Node("Friday")
        self.day_6 = Node("Saturday")
        self.day_7 = Node("Sunday")
        self.day_1.next = self.day_2
        self.day_2.next = self.day_3
        self.day_3.next = self.day_4
        self.day_4.next = self.day_5
        self.day_5.next = self.day_6
        self.day_6.next = self.day_7
        self.day_2.prev = self.day_1
        self.day_3.prev = self.day_2
        self.day_4.prev = self.day_3
        self.day_5.prev = self.day_4
        self.day_6.prev = self.day_5
        self.day_7.prev = self.day_6

    def test_node(self):
        my_log.log.debug("test_node")
        self.assertEqual(self.day_1.data, "Monday")
        self.assertIs(self.day_1.next, self.day_2)
        self.assertIs(self.day_1.prev, None)
        self.assertIs(self.day_7.next, None)

    def test_list(self):
        my_log.log.debug("test_list")
        week = DoublyLinkedList()
        week.head = self.day_1
        self.assertIs(week.head, self.day_1)
        self.assertIs(week.head.next, self.day_2)
        self.assertIs(week.head.prev, None)

        for node in week.generate_list():
            my_log.log.debug(node)

    def test_insert_node_at_front(self):
        my_log.log.debug("test_insert_node_at_front")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.push(data="Sunday")
        self.assertIs(week.head.next, self.day_1)
        self.assertEqual(week.head.data, "Sunday")
        self.assertEqual(week.head.data, self.day_7.data)
        self.assertIsNot(week.head, self.day_7)
        self.assertIs(self.day_1.prev, week.head)

        my_log.log.debug("Push Sunday to front of list")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_insert_node_at_middle(self):
        my_log.log.debug("test_insert_node_at_middle")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.insert_after(prev_node=week.head.next, data="Sunday")
        self.assertIs(week.head, self.day_1)
        self.assertIs(self.day_1.next, self.day_2)
        self.assertEqual(self.day_2.next.data, "Sunday")
        new_node = self.day_2.next
        self.assertIs(new_node.next, self.day_3)
        self.assertIs(new_node.prev, self.day_2)
        self.assertIs(self.day_3.prev, new_node)
        self.assertIs(self.day_2.next, new_node)

        my_log.log.debug("Push Sunday after Tuesday")
        for node in week.generate_list():
            my_log.log.debug(node)

    def test_append_node_to_end(self):
        my_log.log.debug("test_append_node_to_end")
        week = DoublyLinkedList()
        week.head = self.day_1
        week.append(data="Monday")
        self.assertEqual(self.day_7.next.data, "Monday")

        my_log.log.debug("Push Monday to end of list")
        for node in week.generate_list():
            my_log.log.debug(node)

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


if __name__ == '__main__':
    unittest.main()
"""
