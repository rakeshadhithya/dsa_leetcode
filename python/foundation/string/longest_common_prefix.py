#LINK: https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #if lenght of list is 1, then common prefix is whole first word
        firstword = strs[0]
        if len(strs) == 1:
            return firstword   
        #take min_index  
        min_index = len(firstword) - 1
        for i in range(1, len(strs)):
            currword = strs[i]
            curr_max_index = -1
            for j in range(min( len(firstword), len(currword) )):
                if currword[j] == firstword[j]:
                    curr_max_index = max( curr_max_index, j )
                else:
                    break
            if curr_max_index == -1:
                return ''
            min_index = min( min_index, curr_max_index )
        return firstword[: min_index + 1]

'''
if len(strs) = 1: return len(strs[0])
min_end = -1
from 2nd to last
    c_m_e = -1
    for i in range(min(len(word), len(firstword))):
        if word[i] == firstword[i]:
            c_m_e = max(c_m_e, i)
        else:
            break
    m_e = min(m_e, c_m_e)
    if m_e == 0 return 0

m_e = 3
flower
flight
    cme = 1
    2 3 4 5
m_e = 1

    

    
'''