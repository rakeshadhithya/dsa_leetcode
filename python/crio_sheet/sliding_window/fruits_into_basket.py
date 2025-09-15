#LINK: https://leetcode.com/problems/fruit-into-baskets/

#LOGIC: same as longest substring with at most k distinct chars, here that k is 2 
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        dct = {}
        max_len = -float('inf')
        for right in range(len(fruits)):
            dct[fruits[right]] = dct.get(fruits[right], 0) + 1
            while len(dct) > 2:
                dct[fruits[left]] -= 1
                if dct[fruits[left]] == 0:
                    del dct[fruits[left]]
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len