#LINK: https://leetcode.com/problems/happy-number/

class Solution:
    def sumOfSquares(self, n):
        ans = 0
        while n > 0:
            ans += pow(n % 10, 2)
            n //= 10
        return ans
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
        return n == 1

#TC: O(log(10)N) : n iterates through each number in sequence until its 1 or repeated, the max iterations is the
# max number which is 81 * number of digits. no. of digits in a base 10 number is log(10)N
#SC: O(1) : seen stores numbers from 1 to max number, even for 2^31-1 (10 digits) the max is 10 * 81 810 numbers
'''
PIGEON HOLE PRINCIPLE
its a mathematical principle used in combinatorics, If you put n + 1 or more objects into n boxes, 
then at least one box contains more than one object.
Pigeons = steps in the sequence (each new number we generate).
Pigeonholes = the bounded set of possible numbers (values cannot grow indefinitely (bounded by[max number is] 
digit count x 81))'''