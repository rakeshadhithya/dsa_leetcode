#LINK: https://leetcode.com/problems/longest-common-prefix/

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstword = strs[0]
        #for each char in firstword
        for i in range(len(firstword)):
            #for words from 2nd to last
            for j in range(1, len(strs)):
                currword = strs[j]
                #if chr in firstword and currword not equal, return str upto this index
                if i == len(currword) or firstword[i] != currword[i]:
                    return firstword[:i]
        return firstword
#M is length of shortest string
#TC: O(M*N) : i iterates through each char in first string O(M) * j iterates through each str from 2nd till end O(N)
#SC: O(M) : firstword stores ref of first string O(1), currword stores ref of one string at a time till end O(1), 
# firstword[:i] creates a new str upto i which can be shortest string