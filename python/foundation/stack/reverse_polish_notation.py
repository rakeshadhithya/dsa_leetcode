#LINK: https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #take a stack, (list in python)
        stack = [] 
        #from first to last string in list
        for c in tokens:
            # if specific operator, pop -> b , pop -> a push a (operator) b, else push int(c)
            match(c):
                case '+': 
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append( a - b )
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append( int(a / b) )
                case _:
                    stack.append(int(c))
        # if len > 1 then invalid else return last remaining value
        return stack.pop() if len(stack) == 1 else 0
    
#TC: O(N): c iterates through each element O(N)
#SC: O(N): stack stores all elements in worst case