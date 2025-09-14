#LINK: https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        stack = [root]
        while len(stack) != 0:
            #process curr
            curr = stack.pop()
            res.append(curr.val)
            #add right child, so it comes first when popping
            if curr.right != None:
                stack.append(curr.right)
            #add left child
            if curr.left != None:
                stack.append(curr.left)
        return res

        