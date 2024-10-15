import unittest

# Given an array of positive numbers and a positive number 'k,' find the maximum 
# sum of any contiguous subarray of size 'k'.

# Example 1:
# Input: arr = [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:
# Input: arr = [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def maximum_sum_subarrays_of_size_k(arr, K): #O(n)

    window_start = 0
    window_end = 0
    window_sum = 0

    max_window_sum = 0

    while window_end <= len(arr) - 1:
        window_sum += arr[window_end]

        # Slide the window
        if window_end >= K - 1:
            if window_sum >= max_window_sum:
                max_window_sum = window_sum
            
            window_sum -= arr[window_start]
            window_start += 1
        
        window_end += 1
            
    return max_window_sum



class Test(unittest.TestCase):
    def test_1(self):
        output = maximum_sum_subarrays_of_size_k([2, 1, 5, 1, 3, 2], 3)
        expected = 9
        self.assertEqual(output, expected)

    def test_2(self):
        output = maximum_sum_subarrays_of_size_k([2, 3, 4, 1, 5], 2)
        expected = 7
        self.assertEqual(output, expected)

unittest.main()