#LINK: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS: POST ORDER
from typing import Optional
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #if root is null then depth is 0
        if root == None:
            return 0
        #if left child is None return right's minDepth + 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        #if right child is None return left's minDepth + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        #return min(left, right)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
#TC: O(N) : in each node processing takes O(1) * we traverse all nodes O(N)
#SC: O(N) : in each node extra space taken in O(1), recrsiion stack space is O(N) for skewed O(log2(N)) for balanced, 
# max of all is O(N)

'''
     3
 9        20
       15      7

md(20) = min(1, 1) + 1
md(3)  = min(1, 2) + 1  
'''

#BFS: LEVEL ORDER
# for each currsize increment 1 level, before processing that level. after popping node, if both left and right
# childs are None return the level
#TC: O(N) , SC: O(W) <= N/2