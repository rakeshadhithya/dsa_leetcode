#LINK: https://leetcode.com/problems/insert-interval/

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        nl = []
        i = 0
        #add all intervals whose end < start of new interval
        while i < n and intervals[i][1] < newInterval[0]:
            nl.append(intervals[i])
            i += 1
        #from next interval, for all intervals whose start <= end of new interval, update new interval. after all intervals completed append it
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        nl.append(newInterval)
        #add remaining intervals
        while i < n:
            nl.append(intervals[i])
            i += 1
        return nl

#TC: O(N)  : i iterates through each interval using 3 loops O(N) + min and max take O(1)
#SC: O(N)  : nl stores n intervals in worst case O(N)