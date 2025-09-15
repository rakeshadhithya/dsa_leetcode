#LINK: https://leetcode.com/problems/minimum-window-substring/

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        window = {}
        have, needCount = 0, len(need)
        res, resLen = [-1, -1], float("inf")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == needCount:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # shrink window
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""

# TC: O(|s| + |t|) : build need Counter O(|t|) + slide window across s O(|s|) with O(1) dict ops
# SC: O(|s| + |t|) : need stores O(|t|), window stores up to O(|s|) unique chars (bounded by alphabet size Σ)
