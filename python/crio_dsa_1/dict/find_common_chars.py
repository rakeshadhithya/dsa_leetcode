#LINK: https://leetcode.com/problems/find-common-characters/

from typing import List
class Solution:
    #this function will keep the min value of each index of both arrays in array 1 
    def intersection(self, freq1: List[int], freq2: List[int]) -> List[int]: 
        for i in range(26):
            freq1[i] = min( freq1[i], freq2[i] )
        return freq1

    def commonChars(self, words: List[str]) -> List[str]:
        #create array of size 26 to store final freq
        fin_freq = [0] * 26
        #count freq for 1st word in fin_array(1<=words.length<=100)
        for c in words[0]:
            fin_freq[ ord(c) - 97 ] += 1
        #from 2nd to last
        for i in range(1, len(words)):
            #count freq
            freq = [0] * 26
            for c in words[i]:
                freq[ ord(c) - 97 ] += 1
            #keep the min for this and fin_freq in fin_freq
            self.intersection(fin_freq, freq)
        #in fin_freq for each char freq > 0 add that many chars to ans and return
        ans = []
        for i in range(len(fin_freq)):
            while fin_freq[i] != 0:
                ans.append( chr( i+97 ))
                fin_freq[i] -= 1
        return ans

#TC: O(W*C) : i iterates through each word, for each word c iterates through each char, remaining all takes constant 
#SC: O(100) : fin_freq and freq takes constant space 26, ans takes max lenght word(constraint 1 <= words[i].length <= 100)
#this is for problems where using Counter and & is not permitted

'''
Rough:
'bella'  b-1, e-1, l-2, a-1
'label'  l-2, a-1, b-1, e-1
'roller' r-2, o-1, l-2, e-1
ans = e-1, l-2
'''