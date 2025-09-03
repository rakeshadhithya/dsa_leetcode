#LINK: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS: POST ORDER
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #if None depth is 0
        if root == None:
            return 0
        #find left subtree depth, find right subtree depth, return max(left,right) + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#TC: O(N) : in each node processing takes O(1) * total traversed nodes O(N)
#SC: O(N) : in each node extra space created is O(1), recursion stack space is depth of tree O(N) for skewed. take max


'''
   3
9       20
    15     7

max(md(n), md(n)) + 1     md(9) = 1
max(md(9), md(20)) + 1    md(3)
'''


#BFS: LEVEL ORDER
# whenever a currsize loop completed, increment level
#TC: O(N), SC: O(W) <= N