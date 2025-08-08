#Link: https://leetcode.com/problems/rotate-array/description/


# one line solution first k %= nums, take last k elements and first len-k elements and concatenate 
# nums[:] = nums[-k:] + nums[:-k]

#Alternate solution: without any builtin functions using two pointers
from typing import *
class Solution:
    def reverse(self, nums, first, last):
        while( first < last):
            nums[first], nums[last] = nums[last], nums[first] 
            first += 1
            last -= 1 
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for cases k > n, make k within length
        k %= len(nums)
        # reverse whole list
        self.reverse(nums, 0, len(nums)-1)
        # reverse first k digits(k-1)
        self.reverse(nums, 0, k-1)
        # reverse next of kth digit(k) till last
        self.reverse(nums, k, len(nums)-1)
        


'''
Efficiency:
1st sol(reversing):
TC: reverse N elements O(N) , reverse K elements O(k) and reverse N-k elements O(N-k) : O(2N) = O(N)
SC: in place reversal -> O(1)

2nd sol(one line sol):
TC: slice N-k elements O(N-k), slice k elements O(k), concatenate O(N), assigning O(N) : O(3N) = O(N)
SC: new concatenated list O(N) : O(N)
# Though this has higher time and space complexity, it's much faster since Python slicing is 
# vectorized (operates on whole memory chunks at once using low-level C code under the hood).


Learnings:
writing helper functions:
outside of class def to call directly without self it
@staticmethod without self in it to call with class prefix,
inside of class with self to call with self prefix

you don't loops for itarables for basic tasks in python we have 
slice functions, + operator, * operator (all implemented in C and vectorized)

python vectorization:
Many built-in features in Python are vectorized and written in C: list ops (slicing, +, *),
string ops (len, upper, replace), built-ins (sum, min, sorted), set/dict ops (get, in),
and most NumPy/Pandas functions for array/dataframe processing.

'''