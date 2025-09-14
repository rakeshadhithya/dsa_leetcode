#LINK: https://leetcode.com/problems/daily-temperatures/

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                si = stack.pop()
                res[si] = i - si
            stack.append(i)
        return res
#TC: O(N) : res creation O(N) + i, t iterate through each temperature O(N)
#SC: O(N) : stack stores all temperatures when in decreasing order
'''
while iterating through each temp
    we add each temp index to stack
    while curr temp > temp at stack top indices
        update that indices ans to curr index - that index
'''