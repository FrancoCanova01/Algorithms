import unittest

# We are given an array containing n distinct numbers taken from the range 0 to n. Since the 
# array has only n numbers out of the total n+1 numbers, find the missing number.

# Example 1:
# Input: [4, 0, 3, 1]
# Output: 2

# Example 2:
# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7

def missing_number_v3(nums):
    i, n = 0, len(nums)
    while i < n:
      j = nums[i]
      if nums[i] < n and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:
        i += 1

    # find the first number missing from its index, that will be our required number
    for i in range(n):
      if nums[i] != i:
        return i

    return n


class Test(unittest.TestCase):
    def test_1(self):
        output = missing_number_v3([4, 0, 3, 1])
        expected = 2
        self.assertEqual(output, expected)

    def test_2(self):
        output = missing_number_v3([8, 3, 5, 2, 4, 6, 0, 1])
        expected = 7
        self.assertEqual(output, expected)
    
    def test_3(self):
        output = missing_number_v3([0])
        expected = 1
        self.assertEqual(output, expected)

    def test_4(self):
        output = missing_number_v3([0, 1])
        expected = 2
        self.assertEqual(output, expected)

unittest.main()