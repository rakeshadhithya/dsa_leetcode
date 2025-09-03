#LINK: https://leetcode.com/problems/unique-morse-code-words/description/

from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        #store(copy) the given codes given for each lowercase alphabat
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        hashset = set()
        #for each word in words 
        for word in words:
            #create the full code adding each char code and add full code as str to set
            finalcode = []
            for c in word:
                finalcode.append(codes[ord(c) - 97])
            finalcodestr = ''.join(finalcode)  #you can't add list in set
            hashset.add( finalcodestr )
        #return size of set
        return len(hashset)
        
#TC: O(W*C*4) -> O(N*M) where N are total words, M is max chars in a word : 
# word iterates though each word in words, for each word c iterates through each char in word, again for each 
# word join() iterates each coverted char stored in finalcode(4 is max chars in morse_code)
#SC: O(W*C*4) -> O(N*M) where N are total words, M is max chars in word:
# hashset stores all words(W) converted to their char codes (C*4)