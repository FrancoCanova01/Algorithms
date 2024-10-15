import unittest

# Given a sorted array, create a new array containing squares of all the 
# numbers of the input array in the sorted order.

# Example 1:
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]   

# Example 2:
# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]

def makeSquares(arr):
    p1, p2 = 0, len(arr) - 1
    squares = [0 for x in range(len(arr))]
    highestSquaredIndex = len(arr) - 1

    while p1 <= p2:
        sq1 = arr[p1]**2
        sq2 = arr[p2]**2
        if sq1 > sq2:
            squares[highestSquaredIndex] = sq1
            p1 += 1
        else:
            squares[highestSquaredIndex] = sq2
            p2 -= 1
        
        highestSquaredIndex -= 1

    return squares

class TestMakeSquares(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(makeSquares([0, 1, 2, 3, 4]), [0, 1, 4, 9, 16])
        self.assertEqual(makeSquares([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_negative_numbers(self):
        self.assertEqual(makeSquares([-3, -2, -1, 0, 1]), [0, 1, 1, 4, 9])
        self.assertEqual(makeSquares([-5, -4, -3, -2, -1]), [1, 4, 9, 16, 25])

    def test_mixed_numbers(self):
        self.assertEqual(makeSquares([-3, -1, 0, 2, 3]), [0, 1, 4, 9, 9])
        self.assertEqual(makeSquares([-3, -2, -1, 0, 2]), [0, 1, 4, 4, 9])

    def test_zero(self):
        self.assertEqual(makeSquares([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_empty_list(self):
        self.assertEqual(makeSquares([]), [])

if __name__ == '__main__':
    unittest.main()