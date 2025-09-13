#LINK: https://leetcode.com/problems/minimum-size-subarray-sum/description/

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        #build exlusive prefix (n+1 becuase we need to consider n also)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        #for each prefix, find target prefix's left most index where it is >= req, if found update min len
        min_len = float('inf')
        for i in range(n):
            req = prefix[i] + target
            left, right = i + 1, n
            while left <= right:
                mid = (left + right) // 2
                if prefix[mid] >= req:
                    right = mid - 1
                else:
                    left = mid + 1
            if left <= n:
                min_len = min(min_len, left - i)
        return min_len if min_len != float('inf') else 0

#TC: O(NlogN) : building prefix O(N) + i iterates through each number O(N) * for each number binary search from next till end log(N)
#SC: O(N) : prefix stores n elements O(N)

'''
this isn't the “classic” binary search that returns an element index, but instead it's structured to behave like bisect_left:
-We're searching for the first index where prefix[mid] >= required. That's why the loop shrinks right when condition matches (to keep searching left).
-After the loop, left will be at the smallest valid index (j) if one exists
NOTE: binary seach can only be applied on sorted arrays, in prefix array each element is striccly > previous
'''