import unittest 
from linked_list import LinkedList

# Given the head of a Singly LinkedList, write a method
# to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, 
# return the second middle node.

# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# Example 2:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

# Example 3:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4

def middle_of_linked_list(head):

    # Base case that list has one node, the middle is that node
    if head.next is None:
        return head

    result = None

    slow = head
    fast = head

    while True:
        fast = fast.next.next if fast and fast.next else None
        slow = slow.next if slow else None

        if fast is None or fast.next is None:
            # Reached end of list, so return slow pointer
            result = slow
            break
    
    return result


class Test(unittest.TestCase):

    def setup_linked_list(self, ls, cycle_to = None):
        linked_list = LinkedList()
        
        for i in ls:
            linked_list.insert_at_end(i)
        
        if cycle_to != None:
            linked_list.insert_cycle_from_end(cycle_to)

        return linked_list

    def test_1(self):
        linked_list = self.setup_linked_list([1,2,3,4,5])
        middle_node = linked_list.head.next.next
        self.assertEqual(middle_of_linked_list(linked_list.head), middle_node)

    def test_2(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6])
        middle_node = linked_list.head.next.next.next
        self.assertEqual(middle_of_linked_list(linked_list.head), middle_node)

    def test_3(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6,7])
        middle_node = linked_list.head.next.next.next
        self.assertEqual(middle_of_linked_list(linked_list.head), middle_node)
    
    def test_4(self):
        linked_list = self.setup_linked_list([1])
        middle_node = linked_list.head
        self.assertEqual(middle_of_linked_list(linked_list.head), middle_node)

unittest.main()