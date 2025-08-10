# Link: https://leetcode.com/problems/capitalize-the-title/

# ONE LINE SOLUTION using python str functions and list comprehension
# split titile, for each word if len <= 2 convert to lower else convert to capitalize
# return ' '.join([word.lower() if len(word) <= 2 else word.capitalize() for word in title.split()])


#Alternate solution: without any builtin functions using two pointers
class Solution:
    def capitalizeTitle(self, title: str) -> str:
         #convert the given str to list of char's and take 2 ptrs first and last
        char_list = list(title)
        first = 0
        last= 0
        #until last reaches end
        while last < len(char_list):
            #move last to next space making uppercase char's to lowercase
            while last < len(char_list) and char_list[last] != ' ':
                if 65 <= ord(char_list[last]) <= 90:
                    char_list[last] = chr( ord(char_list[last]) + 32)
                last += 1
            #if len of word > 2 and char at first lowercase make it uppercase, move first and last to next word
            if last - first > 2 and 97 <= ord(char_list[first]) <= 122:
                char_list[first] = chr(ord(char_list[first]) - 32)
            first = last + 1
            last += 1
        # convert list to str and return
        return ''.join(char_list)

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

