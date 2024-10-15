import unittest 
from linked_list import LinkedList

# Given the head of a Singly LinkedList, write a function to determine if the 
# LinkedList has a cycle in it or not.

def linked_list_cycle(head): # O(n)
    # You cant just go to the end and see that next is null or 
    # not since you dont know where the end is!

    # Cases:
    # 1) Fast pointer makes it to null. Then there is no cycle.
    # 2) Both pointers enter cycle. Fast pointer eventually approaches slow pointer from
    # behind:
    #   2.1) Fast pointer is one spot behind. Then in next iteration they meet.
    #   2.2) Fast pointer is two spots behind. Then in next iteration you will be in
    #       case 2.1, which means that after that iteration they will meet.

    result = False

    fast = head
    slow = head

    # Loop ends with breaks
    while True:
        fast = fast.next.next if fast and fast.next else None
        slow = slow.next if slow else None

        if fast == None:
            # Reached end of linked list
            result = False
            break

        if slow is fast:
            # Condition for cycle is met
            result = True
            break
    
    return result


class TestLinkedListCycle(unittest.TestCase):

    def setup_linked_list(self, ls, cycle_to = None):
        linked_list = LinkedList()
        
        for i in ls:
            linked_list.insert_at_end(i)
        
        if cycle_to != None:
            linked_list.insert_cycle_from_end(cycle_to)

        return linked_list

    def test_no_cycle(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6])
        self.assertFalse(linked_list_cycle(linked_list.head))
    
    def test_cycle(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6], 3)
        self.assertTrue(linked_list_cycle(linked_list.head))
    
    def test_cycle_one_node(self):
        linked_list = self.setup_linked_list([1], 0)
        self.assertTrue(linked_list_cycle(linked_list.head))
    
    def test_cycle_empty_list(self):
        self.assertFalse(linked_list_cycle(None))

unittest.main()