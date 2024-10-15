import unittest 
from linked_list import LinkedList

# Given the head of a LinkedList with a cycle, find the length of the cycle.

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


class Test(unittest.TestCase):

    def setup_linked_list(self, ls, cycle_to = None):
        linked_list = LinkedList()
        
        for i in ls:
            linked_list.insert_at_end(i)
        
        if cycle_to != None:
            linked_list.insert_cycle_from_end(cycle_to)

        return linked_list
    
    def test_cycle(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6], 3)
        self.assertEqual(linked_list_cycle_length(linked_list.head), 3)
    
    def test_cycle_one_node(self):
        linked_list = self.setup_linked_list([1], 0)
        self.assertTrue(linked_list_cycle_length(linked_list.head), 1)

unittest.main()