#LINK: https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #take odd list and even list
        oh = ot = ListNode()
        eh = et = ListNode()
        #from head to None of given list
        ptr = head
        i = 0
        while ptr:
            i += 1
            #if even index add to even list
            if i % 2 == 0:
                et.next = ptr
                et = et.next
            #else add to odd list
            else:
                ot.next = ptr
                ot = ot.next
            ptr = ptr.next
        #join odd with even, make even end None and return
        ot.next = eh.next
        et.next = None
        return oh.next
#TC: O(N) : ptr iterates through eacch node in given list O(N), ot iterates trough odd indices O(N/2), 
# et iterates through even indices O(N/2). 
#SC: O(1) : oh, eh only creates 2 nodes irrespective of size, and no new node is created anywhere