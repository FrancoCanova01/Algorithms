import unittest
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums= [1, 2, 3, 4]
# Output: false  
# Explanation: There are no duplicates in the given array.

# Example 2:
# Input: nums= [1, 2, 3, 1]
# Output: true  
# Explanation: '1' is repeating.

def containsDuplicate(nums):
    # TODO: Write your code here
    d = {}
    for x in nums:
        keys = d.keys()
        if x in keys:
            d[x] += 1
        else:
            d[x] = 1

        if d[x] >= 2:
            return True

    return False

class TestContainsDuplicate(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(containsDuplicate([1]))

    def test_all_unique_elements(self):
        self.assertFalse(containsDuplicate([1, 2, 3, 4, 5]))

    def test_immediate_duplicate(self):
        self.assertTrue(containsDuplicate([1, 1, 2, 3, 4]))

    def test_duplicate_at_the_end(self):
        self.assertTrue(containsDuplicate([1, 2, 3, 4, 5, 1]))

    def test_large_list_no_duplicates(self):
        large_list_no_duplicates = list(range(10000))
        self.assertFalse(containsDuplicate(large_list_no_duplicates))

    def test_large_list_with_duplicates(self):
        large_list_with_duplicates = list(range(9999)) + [9998]
        self.assertTrue(containsDuplicate(large_list_with_duplicates))

    def test_multiple_duplicates(self):
        self.assertTrue(containsDuplicate([1, 2, 3, 1, 2, 3]))

if __name__ == '__main__':
    unittest.main()