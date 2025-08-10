#LINK: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

class Solution:
    def longest_substring_helper(self, s: str, k: int, start: int, end: int) -> int:
        #base case: if len of substring from start to end < k, then there can't be k chars
        if end-start+1 < k:
            return 0
        #count freq of each char in substring from start to end
        freq = {}
        for i in range(start, end+1):
            c = s[i]
            freq[c] = (0 if c not in freq else freq[c]) + 1
        #remove chars with freq < k divide into left prob and right prob
        for i in range(start, end+1):
            c = s[i]
            if freq[c] < k:
                mid = i
                mid_next = i+1
                while mid_next <= end and freq[s[mid_next]] < k:
                    mid_next += 1
                return max( self.longest_substring_helper(s, k, start, mid-1), 
                            self.longest_substring_helper(s, k, mid_next, end)
                )
        #if all chars freq >= k then return length
        return end - start + 1
    def longestSubstring(self, s: str, k: int) -> int:
        return self.longest_substring_helper(s, k, 0, len(s)-1)

#TC: 
#SC: 