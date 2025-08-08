#LINK: https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        #edge cases for n = 0, n = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        #create list of 2 elements 0 and 1
        list = [0, 1]
        maximum = 1
        #generate new list from 2 to n+1
        for i in range(2, n+1):
            #add element: if index even, then i//2th value else i//2th + i//2+1th values
            if i % 2 == 0:
               list.append( list[i//2] )
            else:
                list.append( list[i//2] + list[i//2 + 1] )
            #update max
            maximum = max( maximum, list[i])
        return maximum