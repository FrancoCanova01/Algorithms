import unittest

# Given an array of sorted numbers, move all non-duplicate number instances at the 
# beginning of the array in-place. The non-duplicate numbers should be sorted and you 
# should not use any extra space so that the solution has constant space complexity i.e., .

# Move all the unique number instances at the beginning of the array and after moving 
# return the length of the subarray that has no duplicate in it.

# Example 1:
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after moving element will be [2, 3, 6, 9].

# Example 2:
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after moving elements will be [2, 11].

def remove(arr):
    if arr == []:
       return 0

    p1 = 0
    p2 = 1

    while p2 != len(arr):
      if arr[p1] != arr[p2]:
        # Swap element next to p1 with p2
        arr[p1 + 1], arr[p2] = arr[p2], arr[p1 + 1]
        # Increment both pointers by one
        p1 += 1
        p2 += 1
      else:
        # Two elements were the same so just move p2
        p2 += 1

    # p1 represents the length of sublist with 
    # unique elements
    return p1 + 1

class TestRemove(unittest.TestCase):
    def test_with_duplicates(self):
        self.assertEqual(remove([1, 1, 2, 2, 3, 4, 4, 5]), 5)
        self.assertEqual(remove([0, 0, 0, 1, 1, 2, 2]), 3)
        self.assertEqual(remove([5, 5, 5, 5]), 1)

    def test_without_duplicates(self):
        self.assertEqual(remove([1, 2, 3, 4, 5]), 5)
        self.assertEqual(remove([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(remove([]), 0)

if __name__ == '__main__':
    unittest.main()