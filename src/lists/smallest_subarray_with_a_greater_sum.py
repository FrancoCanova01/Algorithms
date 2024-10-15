import unittest

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

def smallest_subarray_with_a_greater_sum(arr, s):
    # Start with smallest subarrays and grow from there

    for subarr_length in range(1, len(arr) + 1):
        window_start = 0
        window_end = 0
        window_sum = 0

        while window_end <= len(arr) - 1:
            window_sum += arr[window_end]

            if window_sum >= s:
                return subarr_length
        
            # Slide the window
            if window_end >= subarr_length - 1:
                window_sum -= arr[window_start]
                window_start += 1

            window_end += 1


    return 0


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