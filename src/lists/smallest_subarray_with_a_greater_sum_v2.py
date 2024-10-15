import unittest
import math

# Given an array of positive integers and a number ‘S,’ find the length of 
# the smallest contiguous subarray whose sum is greater than or equal to 'S'. 
# Return 0 if no such subarray exists.

# Example 1:
# Input: arr = [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

# Example 2:
# Input: arr = [2, 1, 5, 2, 8], S=7
# Output: 1 
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# Example 3:
# Input: arr = [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

def smallest_subarray_with_a_greater_sum(arr, s): # O(n)
    # Start with smallest subarrays and dynamically modify the length of the array

    window_start = 0
    window_end = 0
    window_sum = 0
    min_window_length = math.inf

    while window_end <= len(arr) - 1:
        window_sum += arr[window_end]

        if window_sum < s:
            window_end += 1
        else:
            window_length = window_end - window_start + 1

            if window_length  <= min_window_length:
                min_window_length = window_length 
            
            window_sum -= arr[window_start]
            window_sum -= arr[window_end]
            window_start += 1

    return min_window_length if min_window_length != math.inf else 0


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(smallest_subarray_with_a_greater_sum([2, 1, 5, 2, 3, 2], 7), 2)

    def test_2(self):
        self.assertEqual(smallest_subarray_with_a_greater_sum([2, 1, 5, 2, 8], 7), 1)

    def test_3(self):
        self.assertEqual(smallest_subarray_with_a_greater_sum([3, 4, 1, 1, 6], 8), 3)

    def test_4(self):
        self.assertEqual(smallest_subarray_with_a_greater_sum([1, 1, 1, 1, 1], 5), 5)

unittest.main()