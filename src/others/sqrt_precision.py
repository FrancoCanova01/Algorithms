import unittest

def sqrt_precision(x: int, precision: int = 5) -> float:
    
    if x < 0:
        return None

    # Step 1: Calculate integer part
    sqrt_int = 0
    n = 1
    while n < x:
      if ((n + 1)*(n + 1) > x) and n*n <= x:
        sqrt_int = n
      n += 1
    
    # Step 2: Use binary search to approximate decimal part to precision
    left = sqrt_int
    right = sqrt_int + 1
    mid = 0.0

    # Precision control
    increment = 10 ** (-precision)

    while right - left > increment:
        mid = (left + right) / 2
        if mid * mid <= x:
            left = mid
        else:
            right = mid
    
    return round(mid, precision)


class TestMySqrt(unittest.TestCase):
    def test_perfect_squares(self):
        self.assertEqual(sqrt_precision(4,2), 2.01)
        self.assertEqual(sqrt_precision(9, 2), 3.01)
        self.assertEqual(sqrt_precision(16, 2), 4.01)

    def test_non_perfect_squares(self):
        self.assertEqual(sqrt_precision(8, 1), 2.8)
        self.assertEqual(sqrt_precision(15, 1), 3.8)
        self.assertEqual(sqrt_precision(20, 1), 4.4)

    def test_edge_cases(self):
        self.assertEqual(sqrt_precision(0, 3), 0.001)
        self.assertEqual(sqrt_precision(1, 3), 0.999)
        self.assertEqual(sqrt_precision(-1, 3), None)

unittest.main()