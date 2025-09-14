#LINK: https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #create dct1 for list1: add word and and its index
        dct1 = {}
        for i, word in enumerate(list1):
            dct1[word] = i
        #iterate through list2, if word in dct1 calculate index sum
        min_isum = float('inf')
        for i, word in enumerate(list2):
            if word in dct1:
                isum = dct1[word] + i
                #if index sum < prev, update min_isum and create new list with this word
                if isum < min_isum:
                    min_isum = isum
                    res = [word]
                #else if index sum equals min index sum add this word to result
                elif isum == min_isum:
                    res.append(word)
        return res
#TC: O(M+N) : i, word for list1 O(N) + i, word for list2 O(M)
#SC: O(N) : dct1 O(N) + res stores < N O(N)