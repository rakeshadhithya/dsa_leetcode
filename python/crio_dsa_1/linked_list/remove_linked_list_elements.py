#LINK: https://leetcode.com/problems/remove-linked-list-elements/submissions/1733747898/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import *
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #create new head and new tail
        nh = ListNode(0)
        nt = nh
        #iterate with ptr from head till null
        ptr = head
        while( ptr != None ):
            #if ptr.val != val add to new list
            if( ptr.val != val ):
                nt.next = ptr
                nt = nt.next
            #move ptr
            ptr = ptr.next
        nt.next = None
        return nh.next