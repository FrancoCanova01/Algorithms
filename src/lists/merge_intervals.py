import unittest

# Given a list of intervals, merge all the overlapping intervals to produce a 
# list that has only mutually exclusive intervals.

# Example 1:
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

# Example 2:
# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

# Example 3:
# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return (isinstance(other, Interval) and
                self.start == other.start and
                self.end == other.end)

def merge_intervals(intervals): # O(n lon n) (because of sorting)
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key = lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range (1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end) # overlapping intervals, adjust the 'end'
        else:  # non-overlapping interval, add the previous interval and reset
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))
    return merged_intervals


class Test(unittest.TestCase):
    def test_1(self):
        output = merge_intervals([Interval(1,4), Interval(2,5), Interval(7,9)])
        expected = [Interval(1,5), Interval(7,9)]
        self.assertEqual(output, expected)
    
    def test_2(self):
        output = merge_intervals([Interval(6,7), Interval(2,4), Interval(5,9)])
        expected = [Interval(2,4), Interval(5,9)]
        self.assertEqual(output, expected)
    
    def test_3(self):
        output = merge_intervals([Interval(1,4), Interval(2,6), Interval(3,5)])
        expected = [Interval(1,6)]
        self.assertEqual(output, expected)
    
unittest.main()