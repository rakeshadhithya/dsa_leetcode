#Leetcode 252. only avaliable for premuim users
'''
PROBLEM STATEMENT:
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
determine if a person could add all meetings to their schedule without any conflicts.

CONSTRAINTS: 
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000

TEST CASES:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false

Input: intervals = [(5,8),(9,15)]
Output: true
'''

def can_attend_all(intervals):
    #if no meeting, can attend all
    if len(intervals) == 0:
        return True
    #sort based on start time
    intervals.sort(key = lambda x : x[0])
    #for each interval from 2nd, if starttime <= previous endtime then overlap
    previous = intervals[0]
    for i in range(1, len(intervals)):
        current = intervals[i]
        if current[0] <= previous[-1]:
            return False
        previous = current
    return True
intervals = eval(input('Enter the intervals:  '))
print(can_attend_all(intervals))

#TC: 