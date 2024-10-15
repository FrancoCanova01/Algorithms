import unittest
from linked_list import LinkedList

# Given the head of a LinkedList and a number ‘k’, 
# reverse every ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, 
# reverse it too.

def reverse_every_k_element_sub_list(head, k): # O(n)
    # Pre:
    # + Length of linked list is greater than k
    # + Space needs to be O(1) (i cant use arrays to save end of sublists to later connect them)
    result = None

    if head.next == None or k == 1:
        result = head
        return result

    # Find start of sublist, reverse until k is reached (or null)
    # Use that end as start of next sublist and continue
    p1_node = head
    start_prev_sublist = None
    p2_node = head.next
    p2_node_prev = head
    flag = True
    while flag:
        k_counter = 0
        while k_counter < k - 1:
            if p2_node == None: # End of list was reached
                flag = False
                break 

            temp = p2_node.next # Save next before moving pointers
            p2_node.next = p2_node_prev # Move pointer from element in front to previous
            p2_node_prev = p2_node
            p2_node = temp

            k_counter += 1

        # Save new head of list
        if result == None:
            result = p2_node_prev # Last element of first sublist is new head

        # Connect sublists
        if start_prev_sublist != None:
            start_prev_sublist.next = p2_node_prev
        
        # Update start_prev_sublist to be p1_node
        start_prev_sublist = p1_node
        
        # Update start of new sublist if not at end already
        if p2_node != None:
            p1_node = p2_node
            p2_node = p1_node.next
            p2_node_prev = p1_node
    
    # Connect start_prev_sublist to null
    start_prev_sublist.next = None

    return result

class Test(unittest.TestCase):
    def setup_linked_list(self, ls):
        linked_list = LinkedList()
        
        for i in ls:
            linked_list.insert_at_end(i)

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
        linked_list = self.setup_linked_list([1,2,3,4,5,6,7,8])
        output = reverse_every_k_element_sub_list(linked_list.head, 3)
        expected = self.setup_linked_list([3,2,1,6,5,4,8,7])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_2(self):
        linked_list = self.setup_linked_list([2])
        output = reverse_every_k_element_sub_list(linked_list.head, 1)
        expected = self.setup_linked_list([2])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_3(self):
        linked_list = self.setup_linked_list([1,2])
        output = reverse_every_k_element_sub_list(linked_list.head, 2)
        expected = self.setup_linked_list([2,1])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_4(self):
        linked_list = self.setup_linked_list([1, 2, 3, 4])
        output = reverse_every_k_element_sub_list(linked_list.head, 4)
        expected = self.setup_linked_list([4, 3, 2, 1])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_5(self):
        linked_list = self.setup_linked_list([1, 2, 3, 4, 5])
        output = reverse_every_k_element_sub_list(linked_list.head, 1)
        expected = self.setup_linked_list([1, 2, 3, 4, 5])  # No change
        self.assertTrue(self.check_equal(output, expected.head))

    def test_6(self):
        linked_list = self.setup_linked_list([1, 2, 3, 4, 5])
        output = reverse_every_k_element_sub_list(linked_list.head, 2)
        expected = self.setup_linked_list([2, 1, 4, 3, 5])
        self.assertTrue(self.check_equal(output, expected.head))

unittest.main()