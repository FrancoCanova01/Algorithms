import unittest
import math

# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs, here are the indices: (0,3), (0,4), (3,4), (2,5).

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array is a 'good pair'.

# Example 3:
# Input: words = nums = [1,2,3]
# Output: 0
# Explanation: No number is repeating.

def numGoodPairs(nums):
    pairCount = 0
    # TODO: Write your code here
    d = {}
    for i, number in enumerate(nums):
        if number in d.keys():
            d[number].append(i)
        else:
            d[number] = [i]

    good_pairs = 0

    for values in d.values():
        n = len(values)
        k = 2
        if n > 1:
            combinations = math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
            good_pairs += combinations

    return int(good_pairs)

class TestNumGoodPairs(unittest.TestCase):
    def test_repeating_numbers(self):
        self.assertEqual(numGoodPairs([1, 2, 3, 1, 1, 3]), 4)
        self.assertEqual(numGoodPairs([3, 3, 3, 3, 3]), 10)
        self.assertEqual(numGoodPairs([1, 1, 1, 1, 2, 2, 3, 3, 3]), 10)

    def test_non_repeating_numbers(self):
        self.assertEqual(numGoodPairs([1, 2, 3]), 0)
        self.assertEqual(numGoodPairs([5, 6, 7, 8]), 0)

    def test_all_same_numbers(self):
        self.assertEqual(numGoodPairs([1, 1, 1, 1]), 6)
        self.assertEqual(numGoodPairs([5, 5, 5, 5, 5]), 10)

    def test_empty_list(self):
        self.assertEqual(numGoodPairs([]), 0)

if __name__ == '__main__':
    unittest.main()
