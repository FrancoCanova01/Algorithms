import unittest

# Given a list of non-overlapping intervals sorted by their start time, 
# insert a given interval at the correct position and merge all necessary
# intervals to produce a list that has only mutually exclusive intervals.

# Example 1:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

# Example 2:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

# Example 3:
# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return (isinstance(other, Interval) and
                self.start == other.start and
                self.end == other.end)

def insert_interval(intervals, new_interval): #O(n)

    if len(intervals) == 0:
        return []

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    inserted = False

    for i in range(1, len(intervals)):
        # Check if we need to insert interval. Insertion can happen
        # if new_interval.start <= start or also if new_interval_start
        # is between end and start.
        if not inserted and \
            (new_interval.start < start or \
            start <= new_interval.start <= end):
            # Where is end? Depends if there is overlap or not
            if new_interval.end >= start: # Overlap
                start = min(new_interval.start, start)
                end = max(new_interval.end, end)
            else: # No overlap, just insert interval and continue
                merged_intervals.append(Interval(new_interval.start, new_interval.end))
            
            inserted = True

        interval = intervals[i]

        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))

    # Case where interval to be inserted goes at the end
    if not inserted:
        merged_intervals.append(new_interval)

    return merged_intervals


def insert_interval_v2(intervals, new_interval): #O(3n)
    merged = []
    i = 0

    # skip (and add to output) all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i].end < new_interval.start:
      merged.append(intervals[i])
      i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i].start <= new_interval.end:
      new_interval.start = min(intervals[i].start, new_interval.start)
      new_interval.end = max(intervals[i].end, new_interval.end)
      i += 1

    # insert the new_interval
    merged.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
      merged.append(intervals[i])
      i += 1
    
    return merged


class Test(unittest.TestCase):
    def test_1(self):
        output = insert_interval([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4,6))
        expected = [Interval(1,3), Interval(4,7), Interval(8,12)]
        self.assertEqual(output, expected)
    
    def test_2(self):
        output = insert_interval([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4,10))
        expected = [Interval(1,3), Interval(4,12)]
        self.assertEqual(output, expected)
    
    def test_3(self):
        output = insert_interval([Interval(2,3), Interval(5,7)], Interval(1,4))
        expected = [Interval(1,4), Interval(5,7)]
        self.assertEqual(output, expected)

    def test_4(self):
        output = insert_interval([Interval(2,3), Interval(5,7)], Interval(9,11))
        expected = [Interval(2,3), Interval(5,7), Interval(9,11)]
        self.assertEqual(output, expected)
    
    def test_5(self):
        output = insert_interval([Interval(1,2), Interval(3,4), Interval(5,6)], Interval(2,5))
        expected = [Interval(1,6)]
        self.assertEqual(output, expected)

    def test_1_v2(self):
        output = insert_interval_v2([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4,6))
        expected = [Interval(1,3), Interval(4,7), Interval(8,12)]
        self.assertEqual(output, expected)
    
    def test_2_v2(self):
        output = insert_interval_v2([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4,10))
        expected = [Interval(1,3), Interval(4,12)]
        self.assertEqual(output, expected)
    
    def test_3_v2(self):
        output = insert_interval_v2([Interval(2,3), Interval(5,7)], Interval(1,4))
        expected = [Interval(1,4), Interval(5,7)]
        self.assertEqual(output, expected)

    def test_4_v2(self):
        output = insert_interval_v2([Interval(2,3), Interval(5,7)], Interval(9,11))
        expected = [Interval(2,3), Interval(5,7), Interval(9,11)]
        self.assertEqual(output, expected)
    
    def test_5_v2(self):
        output = insert_interval_v2([Interval(1,2), Interval(3,4), Interval(5,6)], Interval(2,5))
        expected = [Interval(1,6)]
        self.assertEqual(output, expected)
    
unittest.main()