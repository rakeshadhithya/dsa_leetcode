#LINK: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            #if open add to stack
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            #else, if stack empty return false or if close and pop not matched return false
            else:
                if len(stack) == 0:
                    return False
                if c == ')' and stack.pop() != '(':
                    return False
                if c == ']' and stack.pop() != '[':
                    return False
                if c == '}' and stack.pop() != '{':
                    return False
        #if not empty false else true
        return True if len(stack) == 0 else False

#TC: O(N) : c iterates through each char O(N)
#SC: O(N) : stack stores all chars in worst case O(N)