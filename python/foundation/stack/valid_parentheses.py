#LINK: https://leetcode.com/problems/valid-parentheses/submissions/1727927852/

class Solution:
    def isValid(self, s: str) -> bool:
        #take stack (in python, list)
        stack = []
        #from 1st to last ch
        for c in s:
            #if open ch push
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            #else if stack empty or pop doesn't match the open ch then flase
            elif len(stack) == 0 or (
                                    c == ')' and stack.pop() != '('  or
                                    c == '}' and stack.pop() != '{'  or
                                    c == ']' and stack.pop() != '['
                                    ):
                return False
        #if stack size not zero then invalid else valid
        return True if len(stack) == 0 else False
    
#TC: O(N) : c  goes through each element in str
#SC: O(N) : stack stores all N elements in worst case