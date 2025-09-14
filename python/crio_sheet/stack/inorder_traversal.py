#LINK: https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while root != None or len(stack) != 0:
            #reach left most root, while adding to stack
            while root != None:
                stack.append(root)
                root = root.left
            #process the current
            curr = stack.pop()
            res.append(curr.val)
            #move right
            root = curr.right
        return res