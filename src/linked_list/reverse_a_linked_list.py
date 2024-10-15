import unittest
from linked_list import LinkedList

# Given the head of a Singly LinkedList, reverse the LinkedList.
# Write a function to return the new head of the reversed LinkedList.

def reverse_a_linked_list(head):
    if not head.next:
        return head

    prev_value = None
    value = head

    while value:
        if value == head: # This could be avoided by just setting next to prev_value!
            temp = value.next
            value.next = None
            value = temp
            prev_value = head
        else:
            temp = value.next
            value.next = prev_value
            prev_value = value
            value = temp

    return prev_value

class Test(unittest.TestCase):
    def setup_linked_list(self, ls, cycle_to = None):
        linked_list = LinkedList()
        
        for i in ls:
            linked_list.insert_at_end(i)
        
        if cycle_to != None:
            linked_list.insert_cycle_from_end(cycle_to)

        return linked_list
    
    def check_equal(self, head_1, head_2):
        p1 = head_1
        p2 = head_2

        while p1 and p2:
            if p1.data != p2.data:
                return False
        
            p1 = p1.next
            p2 = p2.next

        return True 

    def test_1(self):
        linked_list = self.setup_linked_list([2, 4, 6, 8, 10])
        output = reverse_a_linked_list(linked_list.head)
        expected = self.setup_linked_list([10, 8, 6, 4, 2])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_2(self):
        linked_list = self.setup_linked_list([2])
        output = reverse_a_linked_list(linked_list.head)
        expected = self.setup_linked_list([2])
        self.assertTrue(self.check_equal(output, expected.head))

unittest.main()