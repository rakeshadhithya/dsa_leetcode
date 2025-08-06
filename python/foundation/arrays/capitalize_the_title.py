# Link: https://leetcode.com/problems/capitalize-the-title/
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """ 
        # convert the given str to list of char's
        char_list = list(title)
        first = 0
        last= 0
        while last < len(char_list):
            # move last to the first space found
            while last < len(char_list) and char_list[last] != ' ':
                # if last char uppercase make it lowercase
                if 65 <= ord(char_list[last]) <= 90:
                    char_list[last] = chr( ord(char_list[last]) + 32)
                last += 1
            #if word len > 2 and if first char lowercase make it uppercase
            if last - first > 2 and 97 <= ord(char_list[first]) <= 122:
                char_list[first] = chr(ord(char_list[first]) - 32)
            first = last + 1
            last += 1
        # convert list to str and return
        return ''.join(char_list)
    
        # ONE LINE SOLUTION using python str functions and list comprehension
        # split titile, for each word if len <= 2 convert to lower else convert to capitalize
        # return ' '.join([word.lower() if len(word) <= 2 else word.capitalize() for word in title.split()])
    

'''
 Efficiency:
 TC: O(N) -> title converted to list of char O(N), each char iterated once O(N), chars of list joined O(N)
 SC: O(N) -> char_list O(N), returned new joined string O(N)

Learnings:
- for loop in python don't work same as java, changes to ptr inside for loop won't change it as python has for-each only
- use ord() on char to covert to ASCII value, use chr() to covert numeric to char
str class methods:
 - str.join(iterable) will join the elements of a iterable with given str in between
 - str.capitalize() will convert the first char to upper and remaining all to lower
 - str.title() will covert the first char of each word to upper and remaining all to lower

'''

