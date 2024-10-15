import unittest

# We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their 
# creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

# Write a function to sort the objects in-place on their creation sequence number in  without using any extra space. For simplicity, 
# let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

# Example 1:
# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]

# Example 2:
# Input: [2, 6, 4, 3, 1, 5]
# Output: [1, 2, 3, 4, 5, 6]

# Example 3:
# Input: [1, 5, 6, 4, 3, 2]
# Output: [1, 2, 3, 4, 5, 6]

def cyclic_sort(nums): # Time: O(n), Space: O(1)
    position = 0

    while position < len(nums):
        seq_n = nums[position]

        # Put each object in its position by swapping
        temp = nums[seq_n - 1]
        nums[position] = temp
        nums[seq_n - 1] = seq_n

        if seq_n == position + 1:
            position += 1

    return nums

# Worst-case scenario, the while loop will swap a total of n-1 numbers, and 
# once a number is at its correct index, we will move on to the next number 
# by incrementing i. So overall, our algorithm will take O(n) + O(n-1), which is 
# asymptotically equivalent to O(n). During the O(n-1) iterations, position doesn't
# increment, and once it does increment all values are already in place. It does however
# need to increment up until len(nuns) to break the while loop and hence O(n). 

class Test(unittest.TestCase):
    def test_1(self):
        output = cyclic_sort([3, 1, 5, 4, 2])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(output, expected)
    
    def test_2(self):
        output = cyclic_sort([2, 6, 4, 3, 1, 5])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(output, expected)

    def test_3(self):
        output = cyclic_sort([1, 5, 6, 4, 3, 2])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(output, expected)

unittest.main()