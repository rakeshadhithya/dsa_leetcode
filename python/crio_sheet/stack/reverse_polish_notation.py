#LINK: https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            #if not operator, append to stack
            if s not in '+*-/':
                stack.append(s)
            #if operator, pop 2 and append res as per op
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if s == '+':
                    stack.append(a+b)
                elif s == '*':
                    stack.append(a*b)
                elif s == '-':
                    stack.append(b - a)
                else:
                    stack.append( int(b / a))
        return int(stack.pop())
    
#TC: O(N) : s iterates through each token of tokens O(N)
#SC: O(N) : for stack