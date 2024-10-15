import unittest
from linked_list import LinkedList

# Given the head of a LinkedList and two positions ‘p’ and ‘q’, 
# reverse the LinkedList from position ‘p’ to ‘q’.

# The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in Reverse a LinkedList. Here are the steps we need to follow:
# + Skip the first p-1 nodes, to reach the node at position p.
# + Remember the node at position p-1 to be used later to connect with the reversed sub-list.
# + Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
# + Connect the p-1 and q+1 nodes to the reversed sub-list.

def reverse_a_sub_list(head, p, q):
    if head.next is None:
        return head

    # Get to p
    p_pos = 1
    p_node = head
    p_node_prev = head
    while p_pos != p:
        p_node_prev = p_node
        p_node = p_node.next
        p_pos += 1

    # Reverse from p to q
    q_pos = p_pos + 1
    q_node = p_node.next
    q_node_prev = p_node
    while q_pos != q:
        # Update connections
        temp = q_node.next
        q_node.next = q_node_prev

        # Step forward
        q_node_prev = q_node
        q_node = temp
        q_pos += 1

    # Update last connection
    temp = q_node.next
    q_node.next = q_node_prev
    q_node_prev = q_node
    q_node = temp

    # Connect the p_node_prev and q_node nodes to the reversed sub-list.
    p_node_prev.next = q_node_prev
    p_node.next = q_node

    # Whats the new head of the list?
    if p_node == head:
        head = q_node_prev
    
    return head

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
        output = reverse_a_sub_list(linked_list.head, 2, 4)
        expected = self.setup_linked_list([2, 8, 6, 4, 10])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_2(self):
        linked_list = self.setup_linked_list([2])
        output = reverse_a_sub_list(linked_list.head, 2, 2)
        expected = self.setup_linked_list([2])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_3(self):
        linked_list = self.setup_linked_list([2, 3])
        output = reverse_a_sub_list(linked_list.head, 1, 2)
        expected = self.setup_linked_list([3, 2])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_4(self):
        linked_list = self.setup_linked_list([1,2,3,4,5,6])
        output = reverse_a_sub_list(linked_list.head, 1, 4)
        expected = self.setup_linked_list([4,3,2,1,5,6])
        self.assertTrue(self.check_equal(output, expected.head))

    def test_5(self):
        linked_list = self.setup_linked_list([2,1,2,3,4,5,6])
        output = reverse_a_sub_list(linked_list.head, 2, 5)
        expected = self.setup_linked_list([2,4,3,2,1,5,6])
        self.assertTrue(self.check_equal(output, expected.head))

unittest.main()