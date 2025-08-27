#LINK: https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        ans = []
        for i in range(len(s) - len(p) + 1):
            if Counter(s[i : i+len(p)]) == p_count:
                ans.append(i)
        return ans