#LINK: https://leetcode.com/problems/reverse-string/description/
from typing import List
class Solution:
    def reverseStringRecursive(self, s, left, right):
        if left >= right:
            return s
        s[left], s[right] = s[right], s[left]
        return self.reverseStringRecursive(s, left+1, right-1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reverseStringRecursive(s, 0, len(s)-1)

#TC: O(N) : each call O(1) * total calls O(N/2)
#SC: O(N) : each call O(1) * stack depth O(N/2)

'''
Stack Depth and Total calls for a recursive function
Stack Depth : 
'''