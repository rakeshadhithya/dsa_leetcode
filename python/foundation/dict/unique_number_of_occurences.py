#LINK: https://leetcode.com/problems/unique-number-of-occurrences/

#ONE LINE SOLUTION, USING COUNTER CLASS FROM COLLECTIONS MODULE
    # arr_count = Counter(arr)
    # return len(arr_count.values()) == len(set(arr_count.values()))
# Counter object have additional methods like obj.most_common(), also you can add two counter object to find overall count

#Alternate using dict
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #count freq of each num in arr
        dictionary = {}
        for n in arr:
            dictionary[n] = (dictionary[n] if n in dictionary else 0) + 1
        #add each freq to set
        hashset = set(dictionary.values())
        #return if total freq = freq in set
        return len(dictionary.values()) == len(hashset)

#TC: O(N) : n iterates thourgh each element O(N), set() converts dictionary to set O(N)
#SC: O(N) : dictionary takes O(N) in worst case when all unique, hashset takes O(N) in worst case
