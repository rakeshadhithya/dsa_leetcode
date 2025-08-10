#LINK: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #inital window and it's ans's
        hashset = set()
        max_size = 0
        left = 0
        #right from first to last element
        for right in range(len(s)):
            #while right in set, remove left from set and move
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            #add right to set, update ans
            hashset.add(s[right])
            max_size = max(max_size, right-left+1)
        return max_size
    
#Alternate solution (more clarity using while loop and ptrs)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # inital window and it's ans's
        st = set()
        max_size = 0
        left = 0
        # right from first to last element
        for right in range(len(s)):
            # if right not in st add to st, update ans(max that' why after adding)
            if s[right] not in st:
                st.add(s[right])
                max_size = max(max_size, right-left+1)
            # else while right in st remove left and move. add right
            else:
                while s[right] in st:
                    st.remove(s[left])
                    left += 1
                st.add(s[right])
                max_size = max(max_size, right-left+1)
        return max_size
    
#TC: O(N): right moves through each element of list O(N), left moves through each element of list O(N)
#SC: O(N) : set O(N) in worst case