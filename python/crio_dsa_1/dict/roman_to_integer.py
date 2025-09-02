#LINK: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        #map roman symbols to int values
        d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        num = 0
        #for each index
        for i in range(len(s)):
            #if index less than last index and if value of this char < value of next char, decrease value else increment value
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                num -= d[s[i]]
            else:
                num += d[s[i]]
        return num
#TC: O(N) : i iterates each char in roman (O(1) practically since max chars in roman representation is 15)
#SC: O(1) : d stores 7 pairs O(1), num is single digit  (max value for roman in 3999 since no symbol for 5k)