#LINK: https://leetcode.com/problems/remove-linked-list-elements/submissions/1733747898/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #create new head and tail
        nh = nt = ListNode()
        #with ptr traverse from head to null
        ptr = head
        while ptr:
            #if not val add to new linked list
            if ptr.val != val:
                nt.next = ptr
                nt = nt.next
            #move ptr
            ptr = ptr.next
        #make tail of new linked list null, and return head next
        nt.next = None
        return nh.next
#TC: O(N) : ptr iterates through each node from head to none
#SC: O(1) : ptr, nh, nt takes constant time

        '''Alternate Solution, remove in place instead of creating a new linked list'''
        #create a dummy node before head
        dummy = ListNode(0, head)
        #with ptr from dummy to none
        ptr = dummy
        while ptr.next:
            #if ptr.next.val == val, skip and keep next to next.next
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            #else move next
            else:
                ptr = ptr.next 
        #return dummy's next
        return dummy.next
    #TC: O(N) : ptr iterates through each node from head to None
    #SC: O(1) : dummy, ptr takes constant time