#LINK: https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort on end time
        intervals.sort(key = lambda x : x[1])
        #count how many intervals you can keep
        previous = intervals[0]
        count = 1
        #from 2nd if current start >= previous end, no overlap keep it
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] >= previous[1]:
                count += 1
                #update previous only when kept
                previous = current
        #remove count = total - keep count
        return len(intervals) - count
    
#TC: O(NlogN)  : inplace sort method O(NlogN) + i iterates through each interval from 2nd O(N)
#SC: O(1) : all ref's takes constant space O(1)