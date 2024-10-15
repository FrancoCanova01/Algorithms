import unittest
import math

# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.

# Example 1:
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

# Example 2:
# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return (isinstance(other, Interval) and
                self.start == other.start and
                self.end == other.end)



def intervals_intersection_v2(arr1, arr2): # O(N + M) where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.
    intersection = []

    p1 = 0
    p2 = 0

    while (p1 < len(arr1)) and (p2 < len(arr2)): # If one makes it to the end then there is no more chance of intersection after that
        interval1 = arr1[p1]
        interval2 = arr2[p2]

        i1_overlaps_i2 = interval1.start >= interval2.start and interval1.start <= interval2.end
        i2_overlaps_i1 = interval2.start >= interval1.start and interval2.start <= interval1.end

        # Overlap
        if i1_overlaps_i2 or i2_overlaps_i1:
            start = max(interval1.start, interval2.start)
            end = min(interval1.end, interval2.end)
            intersection.append(Interval(start, end))
        
        # Move the pointer which has the interval ending first to the next interval
        if interval1.end < interval2.end:
           p1 += 1
        else:
           p2 += 1

    return intersection

class Test(unittest.TestCase):
    def test_1(self):
        output = intervals_intersection_v2([Interval(1,3), Interval(5,6), Interval(7,9)], [Interval(2,3), Interval(5,7)])
        expected = [Interval(2,3), Interval(5,6), Interval(7,7)]
        self.assertEqual(output, expected)

    def test_2(self):
        output = intervals_intersection_v2([Interval(1,3), Interval(5,7), Interval(9,12)], [Interval(5,10)])
        expected = [Interval(5,7), Interval(9,10)]
        self.assertEqual(output, expected)

unittest.main()