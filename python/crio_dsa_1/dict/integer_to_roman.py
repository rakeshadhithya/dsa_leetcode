#LINK: https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        #map integer values to their roman symbols ordered in descending
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40,'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = []
        #loop through each (value, symbol) pair and extract as many times as that symbol fits into num
        for value, symbol in d:
            count = num // value
            if count:
                roman.append(symbol * count)
                # Reduce num by the value covered
                num -= value * count
        return ''.join(roman)

#TC: O(1) : v,s iterates 13 times O(1), ''.join(roman) iterates at max 15 O(1) 
# (roman representation is bounded num < 3999 because no symbol for 5k and max chars in roman is <= 15)
#SC: O(1) : d stores 13 elements O(1), join creates a str with len <= 15

#WHY list of tuples instead of dict, tuple maintains the order before python 3.7, 
# list of tuples reduces the overhead of hashing, here we are just iterating and not retrieving
#WHY adding to list and then joining, joining is efficient when string is being modified numerous times