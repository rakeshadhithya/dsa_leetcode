#LINK: https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#intuition: remove every node if it has greater value next to it, means in reverse add nodes in incremental fashion, 
# when reversed again no node will have greater value next to it
from typing import Optional
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse list
        head = self.reverse(head)
        #take max=-inf and new list
        max = -float('inf')
        nh = None
        #from head to none
        ptr = head
        while ptr:
            #if val > max, update max, add in reverse fashion, move next
            if ptr.val >= max:
                max = ptr.val
                temp = ptr.next
                ptr.next = nh
                nh = ptr
                ptr = temp
            #else, move next
            else:
                ptr = ptr.next
        return nh
        
    def reverse(self, head):
        nh = None
        ptr = head
        while ptr:
            temp = ptr.next
            ptr.next = nh
            nh = ptr
            ptr = temp
        return nh
    
#TC: O(N) : reverse function traverses each node O(N), ptr traverses each node in reversed list O(N)
#SC: O(1) : reverse function takes O(1), head, max, nh all takes O(1)
'''
dry run
5 2 13 3 8
reverse 8 3 13 2 5
max = 13
newlist: 8 13
'''