import unittest 
from linked_list import LinkedList

# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.

def find_cycle_start(head, meeting_node):
    
    result = None
    
    p1, p2 = head, meeting_node

    # Iterate until p1 is p2
    while True:
        # If p1 made it to meeting node then they didn't 
        # find each other and we need to reset it.
        if p1 is meeting_node and not p1 is p2:
            p1 = head

        if p1 is p2:
            # They met at the start of the cycle
            result = p1
            break
        
        p1 = p1.next
        p2 = p2.next

    return result


def linked_list_cycle_start(head):
    # Once fast and slow meet, reset one pointer to head
    # Move both pointers at same speed. If reseted pointer 
    # gets to "meeting element in cycle", reset again.
    # Iterate like this that eventually they will meet
    # where they meet is the start of the cycle.

    result = None

    # Single node case
    if head.next is head:
        return head
    
    fast, slow = head, head

    while True:
        fast = fast.next.next if fast and fast.next else None
        slow = slow.next

        if fast is slow:
            # They met in the cycle, start cycle beginning search phase
            result = find_cycle_start(head, fast)
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
        linked_list = self.setup_linked_list([1,2,3,4,5,6], 2)
        cycle_start = linked_list.head.next.next
        self.assertEqual(linked_list_cycle_start(linked_list.head), cycle_start)

    def test_cycle_single_node(self):
        linked_list = self.setup_linked_list([1], 0)
        cycle_start = linked_list.head
        self.assertEqual(linked_list_cycle_start(linked_list.head), cycle_start)
    
    def test_cycle_two_nodes(self):
        linked_list = self.setup_linked_list([1, 2], 0)
        cycle_start = linked_list.head
        self.assertEqual(linked_list_cycle_start(linked_list.head), cycle_start)
    
    def test_cycle_at_end(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6], 5)
        cycle_start = linked_list.head.next.next.next.next.next
        self.assertEqual(linked_list_cycle_start(linked_list.head), cycle_start)

unittest.main()