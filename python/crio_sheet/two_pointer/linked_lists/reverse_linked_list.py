#LINK: https://leetcode.com/problems/reverse-linked-list/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nh = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = nh
            nh = curr
            curr = temp
        return nh

#TC: O(N) : curr iterates through each node
#SC: O(1) : all constant space O(1)