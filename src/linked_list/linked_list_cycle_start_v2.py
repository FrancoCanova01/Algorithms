import unittest 
from linked_list import LinkedList

# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.

def linked_list_cycle_length(head): # O(n)
    # If all list has a cycle then the min length is always 1
    result = 1

    fast = head
    slow = head

    saved_slow = None

    # Loop ends with breaks
    while True:
        fast = fast.next.next if fast and fast.next else None
        slow = slow.next if slow else None

        if slow is fast:
            # We are in the cycle, so save slow pointer
            saved_slow = slow

            while saved_slow != slow.next:
                result += 1
                slow = slow.next
            
            break
    
    return result

def linked_list_cycle_start_v2(head): # O(n)
    # Get length of cycle, increase position of p2
    # by that length. Increase both p1,p2 one at a time
    # They will meet at start of cycle.

    # Why Do They Meet at the Cycle Start?
    # The key insight is that pointer2, being K nodes ahead, will complete one full cycle and catch up to pointer1 
    # exactly at the starting point of the cycle: As pointer1 enters the cycle and moves through it, pointer2, which is ahead by K nodes, is also within the cycle 
    # and follows a similar path. Because pointer2 is K nodes ahead, and K is the cycle length, pointer2 will have moved
    # exactly one full cycle ahead of pointer1 by the time they meet. This means that the first place they meet must be the start 
    # of the cycle.

    result = None

    length = linked_list_cycle_length(head)
    
    p1 = head
    p2 = head

    # Iterate p2 to length
    for _ in range(length):
        p2 = p2.next

    while True:
        if p1 is p2:
            # This is the start of the cycle
            result = p1
            break
    
        p1 = p1.next
        p2 = p2.next

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
        self.assertEqual(linked_list_cycle_start_v2(linked_list.head), cycle_start)

    def test_cycle_single_node(self):
        linked_list = self.setup_linked_list([1], 0)
        cycle_start = linked_list.head
        self.assertEqual(linked_list_cycle_start_v2(linked_list.head), cycle_start)
    
    def test_cycle_two_nodes(self):
        linked_list = self.setup_linked_list([1, 2], 0)
        cycle_start = linked_list.head
        self.assertEqual(linked_list_cycle_start_v2(linked_list.head), cycle_start)
    
    def test_cycle_at_end(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6], 5)
        cycle_start = linked_list.head.next.next.next.next.next
        self.assertEqual(linked_list_cycle_start_v2(linked_list.head), cycle_start)

unittest.main()