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

def get_sum_of_square_of_digits(num): # Note on Time Complexity: https://drive.google.com/file/d/1ZFnsAfCwl4WM0YlBerSMwEsqknHwJd9_/view?usp=drive_link
    var_split_square  = [int(i) ** 2 for i in str(num)]
    return sum(var_split_square)

def happy_number_v2(num):
    # Taking a linked list approach with slow and
    # fast pointers. 

    slow_num = num
    fast_num = num

    while True:
        slow = get_sum_of_square_of_digits(slow_num)
        fast = get_sum_of_square_of_digits(get_sum_of_square_of_digits(fast_num))

        if fast == slow:
            if fast == 1 and slow == 1:
                # Stuck in loop with 1 as value
                return True
            else:
                # Equal but not 1 then they are stuck in a bigger loop
                return False
        
        slow_num = slow
        fast_num = fast

class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(happy_number_v2(23))

    def test_2(self):
        self.assertFalse(happy_number_v2(12))

unittest.main()


