#LINK: https://leetcode.com/problems/linked-list-cycle/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


'''
If a cycle exists in a linked list, then two pointers moving at different speeds will eventually meet inside
the cycle — just like two runners on a circular track
If there's no cycle, fast will reach the end (None)
If there's a cycle, fast will eventually "lap" slow and they will meet
'''