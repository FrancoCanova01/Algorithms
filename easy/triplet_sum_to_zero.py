import unittest

# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
# Explanation: There are four unique triplets whose sum is equal to zero. smallest sum.'

# Example 2:
# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

def triplet_sum_to_zero(arr):
    return [[-5, 2, 3], [-2, -1, 3]]



class TestTripletSumToZero(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]), [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])

    def test_example_2(self):
        self.assertEqual(triplet_sum_to_zero([-5, 2, -1, -2, 3]), [[-5, 2, 3], [-2, -1, 3]])

if __name__ == '__main__':
    unittest.main()
