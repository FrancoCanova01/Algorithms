import unittest

# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.

# Example 1:
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 7]
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



def intervals_intersection(arr1, arr2):
    # Get upper bound
    m = max(arr1[-1].end, arr2[-1].end)
    freq_count = [0] * m

    # Iterate over arr1 and fill freq_count
    for interval in arr1:
        rng = range(interval.start, interval.end + 1)
        for num in rng:
            freq_count[num - 1] += 1

    # Iterate over arr2 and fill freq_count
    for interval in arr2:
        rng = range(interval.start, interval.end + 1)
        for num in rng:
            freq_count[num - 1] += 1

    # Iterate over freq_count and get intersections
    intersection = []

    p1 = 0
    p2 = 0

    while p1 < len(freq_count):
        if freq_count[p1] == 2:
            start = p1
            p2 = p1

            while freq_count[p2] == 2:
                p2 += 1
        
            end = p2 - 1
            intersection.append(Interval(start + 1, end + 1))
            p1 = end + 1
        else:
            p1 += 1

    return intersection

# Time Complexity: O(N * n + M * m + Z)
# - Fill freq count: O(N * n) where N is the size of arr1
# and n is the max length/span of any given interval
# - Fill freq count: O(M * m) where M is the size of arr2
# and m is the max length/span of any given interval
# - Iterate over Z (maximum number in all given intervals)

# Space Complexity: O(Z)
# Increased space complexity O(Z) since we create an array of 
# Z spaces where Z is the maximum number in all given intervals

class Test(unittest.TestCase):
    def test_1(self):
        output = intervals_intersection([Interval(1,3), Interval(5,6), Interval(7,9)], [Interval(2,3), Interval(5,7)])
        expected = [Interval(2,3), Interval(5,7)]
        self.assertEqual(output, expected)

    def test_2(self):
        output = intervals_intersection([Interval(1,3), Interval(5,7), Interval(9,12)], [Interval(5,10)])
        expected = [Interval(5,7), Interval(9,10)]
        self.assertEqual(output, expected)

unittest.main()