import unittest

# Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

# Pre: Non empty list, K > 0
def avg_of_k_elements(arr, K): # O(n)
    result = []

    window_start = 0
    window_end = 0
    window_sum = 0

    # Slide the window
    while window_end <= len(arr) - 1:
        window_sum += arr[window_end]

        if window_end >= K - 1:
            result.append(round(window_sum / K, 1))
            window_sum -= arr[window_start]
            window_start += 1

        window_end += 1

    return result


class Test(unittest.TestCase):
    def test_one_element_list(self):
        self.assertEqual(avg_of_k_elements([1], 1), [1])

    def test_window_size_one(self):
        self.assertEqual(avg_of_k_elements([1,2,3,4,5], 1), [1,2,3,4,5])
    
    def test_complex(self):
        self.assertEqual(avg_of_k_elements([1, 3, 2, 6, -1, 4, 1, 8, 2], 5), [2.2, 2.8, 2.4, 3.6, 2.8])

if __name__ == '__main__':
    unittest.main()