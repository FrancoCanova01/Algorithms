import unittest

# Given an array of numbers sorted in ascending order and a target sum, find a 
# pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers 
# (i.e. the pair) such that they add up to the given target. If no such pair exists return [-1, -1].

# Example 1:
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

# Example 2:
# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

def search(arr, target_sum):
    p1 = 0
    p2 = len(arr) - 1

    while p1 < p2:
        sum = arr[p1] + arr[p2]
        if sum == target_sum:
            return [p1, p2]
        elif sum < target_sum:
            p1 += 1
        else:
            p2 -= 1

    return [-1, -1]

class TestSearch(unittest.TestCase):
    def test_valid_pairs(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 9), [3, 4])
        self.assertEqual(search([2, 4, 6, 8, 10], 10), [0, 3])

    def test_invalid_pairs(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 20), [-1, -1])
        self.assertEqual(search([2, 4, 6, 8, 10], 7), [-1, -1])

    def test_negative_numbers(self):
        self.assertEqual(search([-3, -1, 0, 2, 4], 1), [0, 4])
        self.assertEqual(search([-5, -3, -2, 0, 2, 5], -1), [1, 4])

    def test_zero(self):
        self.assertEqual(search([0, 1, 2, 3, 4], 0), [-1, -1])

    def test_empty_list(self):
        self.assertEqual(search([], 5), [-1, -1])

if __name__ == '__main__':
    unittest.main()