#LINK: https://leetcode.com/problems/merge-intervals/

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals on start time
        intervals.sort(key = lambda x: x[0])
        #add 1st interval to new list
        nl = [intervals[0]]
        #from 2nd interval
        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            #if start <= new list's end, update nl end to max of curr end, nl end
            if s <= nl[-1][-1]:
                nl[-1][-1] = max(nl[-1][-1], e)
            #else add interval to new list
            else:
                nl.append([s,e])
        return nl
    
#TC: O(NlogN)  : inplace sort method O(NlogN) + i iterates through each interval O(N)
#SC: O(N) : nl stores as many as intervals in worst case O(N)
        
'''
[1,3], [2, 6] , [8,10], [15,18]

nl = [1, 3]
s, efrom 2nd
    if s <= nl_e:
        nl_e = c_e
    else:
        add s,e to nl
nl = [1, 6], [8, 10], [15, 18]

[1,4], [4, 5]
nl = [1,5]

'''