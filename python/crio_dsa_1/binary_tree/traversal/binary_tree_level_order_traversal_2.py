#LINK: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from queue import Queue
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: 
            return []
        #take ans list, queue and put root
        ans = []
        queue = Queue()
        queue.put(root)
        #while queue not empty
        while not queue.empty():
            #take currsize, currlist
            currsize = queue.qsize()
            currlist = []
            #for currsize times
            for i in range(currsize):
                #pop node, process(add to currlist)
                node = queue.get()
                currlist.append(node.val)
                #if not null add left child
                if node.left:
                    queue.put(node.left)
                #if not null add right child
                if node.right:
                    queue.put(node.right)
            #add currlist to ans (you can insert at beginning each time for direct reversal but it takes O(N) each time
            ans.append(currlist)
        #reverse and return ans
        ans.reverse()
        return ans
    
#TC: each node is enqued and dequed exactly once O(N) * all functions for node processing takes O(1), 
# at last reversal takes O(Levels). N + L
#SC: ans stores all nodes O(N), queue stores at most one level O(width) <= O(N/2), currlist stores at
#  most one level O(width) <= O(N/2). max(N + N/2 + N/2) [maximum simultaneous usage]

'''
    3
  9    20
     15   7

ans: [[3], [9, 20], [15, 7]]
queue: 
currsize: 0
currlist: [15, 7]

reverse and return ans
'''