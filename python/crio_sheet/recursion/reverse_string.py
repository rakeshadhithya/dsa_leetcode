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
total calls and stack depth for recursive functions:
total calls : how much the problem shrinks per call : if it shrinks by 1 - N calls, if it shrinks by 2 - N/2 calls,
              if it shrinks by half i.e. N/2 - log2N calls
stack depth : longest chain of calls : if one recursive call - depth is no. of calls, else b^total calls (b is branching factor i.e. no. of recursive calls)
'''


'''
never go by recursive calls, it's all confusing and wastes lot of time without conclusion.
go by how much the problem is shrinking per call and longest chain of calls. if branching factor > 1 
simply time becomes b^totalcalls and space becomes just totalcalls for least shrinking
'''

'''
total calls : Depends on branching factor (b) and how much the problem shrinks per call.
If b = 1 (linear recursion):
    Total calls = number of steps until base case
    Shrinks by 1 → O(N)
    Shrinks by 2 → O(N/2)
If b > 1 (branching recursion):
    Total calls ≈ O(b^d)
    where d = depth = number of steps until base case

Shrinks by half → O(log N)
    if b = 1 : 
    if b > 1 : b ^ d (depth = no. of steps till base case)
stack depth : longest chain of calls 
    if b = 1 : depth = total calls
    if b > 1 : depth = 
'''