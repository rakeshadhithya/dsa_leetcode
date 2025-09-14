
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])
#TC: O(NlogN) : list comprehention O(N) + sorted O(NlogN)
#SC: O(N) : new list from comprehention O(N) + sorted creates another list O(N)
        