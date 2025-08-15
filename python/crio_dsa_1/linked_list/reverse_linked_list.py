#LINK: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #take nh
        nh = None
        #ptr from head to None
        ptr = head
        while ptr:
            #store ptr.next
            temp = ptr.next
            #ptr.next points to nh
            ptr.next = nh
            #nh moves to ptr, ptr moves to stored ptr.next
            nh = ptr
            ptr = temp
        return nh
#TC: O(N) : ptr iterates from head to None
#SC: O(1) : ptr, temp, nh all take constant time