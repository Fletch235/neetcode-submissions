"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_sorted = sorted(intervals, key = lambda x: x.start)

        for i in range(1, len(intervals_sorted)):
            i1 = intervals_sorted[i - 1]
            i2 = intervals_sorted[i]
            if i1.end > i2.start:
                return False

        return True