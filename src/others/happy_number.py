import unittest

# Any number will be called a happy number if, after repeatedly replacing
# it with a number equal to the sum of the square of all of its digits, 
# leads us to the number 1. All other (not-happy) numbers will never reach 
# 1. Instead, they will be stuck in a cycle of numbers that does not include 1.

# Given a positive number n, return true if it is a happy number otherwise 
# return false.

# Example 1:
# Input: 23
# Output: true (23 is a happy number)
# Explanations: Here are the steps to find out that 23 is a happy number:
#  2^2 + 3^2 = 4 + 9 = 13
#  1^2 + 3^2 = 1 + 9 = 10
#  1^2 + 0^2 = 1 + 0 = 1

# Example 2:
# Input: 12
# Output: false (12 is not a happy number)
# Explanations: Here are the steps to find out that 12 is not a happy number:

#  = 1 + 4 = 5
# = 25
#  = 4 + 25 = 29
#  = 4 + 81 = 85
#  = 64 + 25 = 89
#  = 64 + 81 = 145
#  = 1 + 16 + 25 = 42
#  = 16 + 4 = 20
#  = 4 + 0 = 4
#  = 16
#  = 1 + 36 = 37
#  = 9 + 49 = 58
#  = 25 + 64 = 89

# Please note the cycle from 89 -> 89.

def happy_number(num): # O(n * m)
    # Can a calculation of squares be repeated without presence of a loop? 
    #   No: If a calculation is repeated then all subsequent calculations will be repeated
    #   until we get to the loop. So repeating a calculation means we are in a loop.

    var = num
    values = set()

    while var != 1:
        var_split = [int(i) for i in str(var)]
        var_split_square = [i ** 2 for i in var_split]
        var_split_sum = sum(var_split_square)

        if var_split_sum in values:
            # Cycle encountered
            return False
        
        values.add(var_split_sum)
        var = var_split_sum

    return True


class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(happy_number(23))

    def test_2(self):
        self.assertFalse(happy_number(12))

unittest.main()