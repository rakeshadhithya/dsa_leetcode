#LINK: https://leetcode.com/problems/same-tree/
 
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs_pre(self, node1, node2):
        #if noth are none then true, if any is None then false
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False
        #if values not equal fasle, else find on left and right
        if node1.val != node2.val:
            return False
        return self.dfs_pre(node1.left, node2.left) and self.dfs_pre(node1.right, node2.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs_pre(p,q)
    
# TC: O(N) : each node visited once
# SC: O(H) : recursion depth, O(N) in worst case (skewed tree), O(log N) for balanced tree
