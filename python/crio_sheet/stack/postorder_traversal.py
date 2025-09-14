#LINK: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # preorder N L R , slight change N R L, so when reversed gives postorder: L R N
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        prestack = [root]
        res = []
        while len(prestack) != 0:
            curr = prestack.pop()
            res.append(curr.val)
            if curr.left != None:
                prestack.append(curr.left)
            if curr.right != None:
                prestack.append(curr.right)
        return [n for n in reversed(res)]