#LINK: https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS: POST ORDER
from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #if null count is 0
        if root == None:
            return 0
        #find left count, find right count return lc + rc + 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    
#TC: O(N) : in each node, processing takes O(1) * total traversed nodes O(N)
#SC: O(N): in each node no extra spaces O(1), recursion stack stores depth of tree i.e. log2(N) if balanced, N if 
# skewed O(N), take the max one because space overlaps in time 

'''
     1
  2      3
4   5  6

1 + c(4) + c(5)
1 + c(2) + c(3)
'''

#BFS: LEVEL ORDER
#whenever you pop node, increment count
#TC: O(N), SC: O(W) i.e <= N/2