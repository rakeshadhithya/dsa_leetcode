#LINK: https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
from typing import Optional
class Solution:
    def length(self, head):
        count = 0
        ptr = head
        while ptr != None:
            count += 1
            ptr = ptr.next
        return count

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #find the len of list
        ll_length = self.length(head)
        #traverse to mid len
        ptr = head
        for _ in range(ll_length//2):
            ptr = ptr.next
        return ptr
#TC: O(N) : length function takes O(N), _ traverses till midlen (ON)
#SC: O(1) : ll_length, ptr, count all take constant space


#using fast and slow pointers
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #fast and slow pointers
    fast = slow = head
    #until fast and fast.next not None
    while fast and fast.next:
        #move fast 2 times, slow 1 time
        fast = fast.next.next
        slow = slow.next
    #return slow
    return slow
#TC: O(N) : fast takes O(N/2) time (slow also same)
#SC: no extra space