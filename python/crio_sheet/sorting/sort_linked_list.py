#LINK: https://leetcode.com/problems/sort-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    #merge two ll
    def merge(self, l1, l2):
        nh = ListNode(0)
        nt = nh
        while l1 and l2:
            if l1.val < l2.val:
                nt.next = l1
                l1 = l1.next
            else:
                nt.next = l2
                l2 = l2.next
            nt = nt.next
        nt.next = l2 or l1
        return nh.next
    #find mid of ll
    def mid(self, l):
        slow, fast = l, l.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if 0 or 1 node return
        if head == None or head.next == None:
            return head
        #divide list into two halves, sort left & store and same for right
        md = self.mid(head)
        right = md.next
        md.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)
        #merge sorted arrays
        return self.merge(left_sorted, right_sorted)

# TC: O(n log n) : each level of recursion splits list in half log n levles and merging two lists takes O(n) 
# SC: O(log n) : recursion stack depth = log n, merging done in-place, only constant pointers used
