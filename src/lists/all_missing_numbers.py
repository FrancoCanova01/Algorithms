import unittest

# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
# The array can have duplicates, which means some numbers will be missing. Find all
# those missing numbers.

# Example 1:
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

# Example 2:
# Input: [2, 4, 1, 2]
# Output: 3

# Example 3:
# Input: [2, 3, 2, 1]
# Output: 4

def all_missing_numbers(nums): # O(n)
    p1 = 0
    seen = set()

    while p1 < len(nums):
        val = nums[p1]

        temp = nums[val - 1]
        nums[val - 1] = val
        nums[p1] = temp

        # Is in position or its been seen before
        if p1 + 1 == nums[p1] or nums[p1] in seen:
            p1 += 1
          
        seen.add(val)

    result = []

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            result.append(i + 1)

    return result


class Test(unittest.TestCase):
    def test_1(self):
        output = all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1])
        expected = [4, 6, 7]
        self.assertEqual(output, expected)

    def test_2(self):
        output = all_missing_numbers([2, 4, 1, 2])
        expected = [3]
        self.assertEqual(output, expected)
    
    def test_3(self):
        output = all_missing_numbers([2, 3, 2, 1])
        expected = [4]
        self.assertEqual(output, expected)

unittest.main()