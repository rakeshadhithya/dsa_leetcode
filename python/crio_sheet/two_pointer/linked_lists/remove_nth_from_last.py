#LINK: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        #move fast n times
        for _ in range(n):
            fast = fast.next
        #if fast is None, then head is the one to remove
        if fast == None:
            return head.next
        #if nth from last then total - n from start, fast moved n times, remaining are total - n. move both fast and slow one at a time till fast reached last node, slow will be one node before the node to remove
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
    
#TC: O(N) : fast iterates through each node O(N), slow does not iterate it moves 1 step with fast 
#SC: O(1) : all constant space O(1)