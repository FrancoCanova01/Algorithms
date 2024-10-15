import unittest

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.8284, and since we need to return the floor of the square root (integer), hence we returned 2.  

# Example 2:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2.

# Example 3:
# Input: x = 2
# Output: 1
# Explanation: The square root of 2 is 1.414, and since we need to return the floor of the square root (integer), hence we returned 1.  

def mySqrt(x: int) -> int:
    # TODO: Write your code here
    n = 1
    while n < x:
      if ((n + 1)*(n + 1) > x) and n*n <= x:
        return n
      n += 1

    return 0

class TestMySqrt(unittest.TestCase):
    def test_perfect_squares(self):
        self.assertEqual(mySqrt(4), 2)
        self.assertEqual(mySqrt(9), 3)
        self.assertEqual(mySqrt(16), 4)

    def test_non_perfect_squares(self):
        self.assertEqual(mySqrt(8), 2)
        self.assertEqual(mySqrt(15), 3)
        self.assertEqual(mySqrt(20), 4)

    def test_edge_cases(self):
        self.assertEqual(mySqrt(0), 0)
        self.assertEqual(mySqrt(1), 0)
        self.assertEqual(mySqrt(-1), 0)

if __name__ == '__main__':
    unittest.main()