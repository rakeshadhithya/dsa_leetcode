#LINK: https://leetcode.com/problems/split-linked-list-in-parts/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#intuition: k parts needed, each part has size//k elements, first size % k elements contain 1 extra element. 
# (works for both k < size and k > size)

from typing import Optional, List
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        #take ans list, size, counter = 0, ptr = head
        ans = []
        size = self.size(head)
        c = 0
        ptr = head
        #for k times
        for i in range(k):
            #increment counter(nth node), add ptr to ans list
            c += 1
            ans.append(ptr)
            #if counter <= size % k, elements is size//k + 1 else size//k
            elements = size//k + 1 if c <= size % k else size//k
            #move ptr elements-1 times(bcoz already starting from head)
            for i in range(elements-1):
                ptr = ptr.next
            #if ptr not None make it's next None by storing in temp, else it remains None
            if ptr != None:
                temp = ptr.next
                ptr.next = None
                ptr = temp
        return ans
    def size(self, head):
        c = 0
        ptr = head
        while ptr:
            c += 1
            ptr = ptr.next
        return c

#TC: O(max(k, size)) : i iterates k times O(k). for each i, ptr moves through size//k times(+1 ignore), when size finished 
'''
k = 2
      p
1 2 3
c = 3
ans = 1->n, 2->n, 3->n, n
s = 1
'''