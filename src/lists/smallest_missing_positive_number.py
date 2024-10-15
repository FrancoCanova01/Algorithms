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

def smallest_missing_positive_number(nums):
    freq = [0] * max(nums)

    for i in nums:
        if i <= 0:
            continue
        else:
            freq[i - 1] = 1

    for index, i in enumerate(freq):
        if i == 0:
            return index + 1

    # Based on pre condition this return is never executed.
    return max(nums) + 1


class Test(unittest.TestCase):
    def test_1(self):
        output = smallest_missing_positive_number([-3, 1, 5, 4, 2])
        expected = 3
        self.assertEqual(output, expected)
    
    def test_2(self):
        output = smallest_missing_positive_number([3, -2, 0, 1, 2])
        expected = 4
        self.assertEqual(output, expected)

    def test_3(self):
        output = smallest_missing_positive_number([3, 2, 5, 1])
        expected = 4
        self.assertEqual(output, expected)

    def test_4(self):
        output = smallest_missing_positive_number([33, 37, 5])
        expected = 1
        self.assertEqual(output, expected)

unittest.main()
