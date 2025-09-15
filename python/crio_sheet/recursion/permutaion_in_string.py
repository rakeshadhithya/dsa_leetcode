#LINK: https://leetcode.com/problems/permutation-in-string/

#RECURSIVE SOLUTION (NOT OPTIMAL)
from collections import Counter
class Solution:
    def helpInclusion(self, s2, n, i, s1_counter):
        if i + n > len(s2):
            return False
        if Counter(s2[ i : i + n ]) == s1_counter:
            return True
        return self.helpInclusion(s2, n, i + 1, s1_counter)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        return self.helpInclusion(s2, len(s1), 0, s1_counter)
# TC: O(n * m) – build Counter for each of m-n+1 windows
# SC: O(n + m) – Counter storage + recursion depth



#SLIDING WINDOW(MOST OPTIMISED)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case
        if len(s1) > len(s2):
            return False
        #target
        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        #initial window
        curr_map = {}
        for i in range(len(s1)):
            curr_map[s2[i]] = curr_map.get(s2[i], 0) + 1
        #compare ans
        if curr_map == s1_map:
            return True
        left = 0
        #slide the window
        for right in range(len(s1), len(s2)):
            curr_map[s2[right]] = curr_map.get(s2[right], 0) + 1
            curr_map[s2[left]] = curr_map.get(s2[left]) - 1
            if curr_map[s2[left]] == 0:
                del curr_map[s2[left]]
            left += 1
            if curr_map == s1_map:
                return True
        return False
    
# TC: O(n + m) : build maps O(n), slide window across m characters
# SC: O(Σ) : hashmap for counts (constant if alphabet fixed, e.g., 26 letters)

    
