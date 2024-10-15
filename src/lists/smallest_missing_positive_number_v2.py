import unittest

# Given an unsorted array containing numbers, find the smallest missing positive number in it.
# Note: Positive numbers start from '1'.

# Example 1:
# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'

# Example 2:
# Input: [3, -2, 0, 1, 2]
# Output: 4

# Example 3:
# Input: [3, 2, 5, 1]
# Output: 4

# Example 4:
# Input: [33, 37, 5]
# Output: 1

def smallest_missing_positive_number_v2(nums): # O(n)
    p1 = 0
    seen = set()

    while p1 < len(nums):
        value = nums[p1]
        if value <= 0 or value >= len(nums) or value in seen: # Negative numbers or numbers out of bounds of nums
            p1 += 1
            continue
        else:
            temp = nums[value - 1]
            nums[value - 1] = value
            nums[p1] = temp

            if nums[p1] == p1 + 1: # Value was placed in correct slot, then advance.
                p1 += 1
            
            seen.add(value)

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1

    # Went over all list and all values are there, so missing number is the next in the list
    return len(nums) + 1

class Test(unittest.TestCase):
    def test_1(self):
        output = smallest_missing_positive_number_v2([-3, 1, 5, 4, 2])
        expected = 3
        self.assertEqual(output, expected)
    
    def test_2(self):
        output = smallest_missing_positive_number_v2([3, -2, 0, 1, 2])
        expected = 4
        self.assertEqual(output, expected)

    def test_3(self):
        output = smallest_missing_positive_number_v2([3, 2, 5, 1])
        expected = 4
        self.assertEqual(output, expected)

    def test_4(self):
        output = smallest_missing_positive_number_v2([33, 37, 5])
        expected = 1
        self.assertEqual(output, expected)

    def test_5(self):
        output = smallest_missing_positive_number_v2([-3, 1, 2, 5, 4, 2])
        expected = 3
        self.assertEqual(output, expected)

unittest.main()