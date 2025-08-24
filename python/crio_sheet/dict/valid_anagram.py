#LINK: https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #count frequenices using 26 size array, iterate it return false when freq not same
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in s:
            freq1[ ord(c) - 97 ] += 1
        for c in t:
            freq2[ ord(c) - 97 ] += 1
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True
    
#TC: O(N + M) N and M are same length so O(N) : c iterates through each char in s O(N), another c iterates through 
# each char in t O(M). i takes constant time
#SC: O(1) : freq1 takes constant space O(26), freq2 takes constant space O(26)

#ALTERNATE SOLUTIONS:
#1. You can use Counter function and ==
#2. You can use count method 

'''
anagram, nagaram
a - 2, n - 1, g - 1, r - 1, m - 1
a - 2, n - 1, g - 1, r - 1,  m - 1
'''

