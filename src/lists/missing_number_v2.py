import unittest

# We are given an array containing n distinct numbers taken from the range 0 to n. Since the 
# array has only n numbers out of the total n+1 numbers, find the missing number.

# Example 1:
# Input: [4, 0, 3, 1]
# Output: 2

# Example 2:
# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7

def missing_number_v2(nums):
    # Apply cyclic sort, if number exceeds its index then ignore
    # Check where prev number does not equal next number + 1. If
    # that happens then the missing number is at that index + 1
    p1 = 0

    while p1 < len(nums):
        val = nums[p1]

        if val >= len(nums):
            p1 += 1
            continue
        
        temp = nums[val]
        nums[p1] = temp
        nums[val] = val

        if p1 == val:
            p1 += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i 

    # Based on precondition, this return statement will never be executed
    return 0


class Test(unittest.TestCase):
    def test_1(self):
        output = missing_number_v2([4, 0, 3, 1])
        expected = 2
        self.assertEqual(output, expected)

    def test_2(self):
        output = missing_number_v2([8, 3, 5, 2, 4, 6, 0, 1])
        expected = 7
        self.assertEqual(output, expected)

unittest.main()