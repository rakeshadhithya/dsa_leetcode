#LINK: https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)
        #if len(p) > len(s) then not possible
        if p_len > s_len:
            return []
        #count p, take window till p len, slide the window compare and append
        s_indices = []
        p_count = Counter(p)
        window = Counter(s[:p_len])
        if p_count == window:
            s_indices.append(0)
        for right in range(p_len, s_len):
            left = right - p_len
            window[s[right]] += 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            if window == p_count:
                s_indices.append(left + 1)
        return s_indices
#TC: O(P + S)  : len function O(1) + Counter(p) O(P) + s[:p_len] O(P) + Counter(s[:p_len]) O(P) +
#  p_count == window O(1) since limited chars + 
# (right from p_len to s_len O(S) since len(s) > len(p) * window == p_count O(1) since limited chars)
#SC: O(S) : s[:p_len] O(P), s_indices O(S) when p_len = 1, p_count and window O(1) since limited chars. 
# max of all is O(S) since len(s) > len(p)