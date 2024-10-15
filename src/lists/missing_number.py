import unittest

# We are given an array containing n distinct numbers taken from the range 0 to n. Since the 
# array has only n numbers out of the total n+1 numbers, find the missing number.

# Example 1:
# Input: [4, 0, 3, 1]
# Output: 2

# Example 2:
# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7

def missing_number(nums): # O(n)
    # Create array of empty values
    freq_count = [0] * (len(nums) + 1)

    for i in nums:
        freq_count[i] = 1

    for index, i  in enumerate(freq_count):
        if i == 0:
            return index
    
    # Because of pre condition it might not even get here
    return None

class Test(unittest.TestCase):
    def test_1(self):
        output = missing_number([4, 0, 3, 1])
        expected = 2
        self.assertEqual(output, expected)

    def test_2(self):
        output = missing_number([8, 3, 5, 2, 4, 6, 0, 1])
        expected = 7
        self.assertEqual(output, expected)

unittest.main()