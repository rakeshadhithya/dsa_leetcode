#LINK: https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow




'''
fast moves 2 steps ahed, slow moves 1 step
when fast reaches end, slow has covered half the path
'''