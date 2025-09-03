#LINK: https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#DFS: POST ORDER 
#Intuition is if unbalanced return -1 else height
from typing import Optional
class Solution:
    def findHeight(self, root):
        #if root is None then height is 0
        if root == None:
            return 0
        #find left height, if -1 terminate early i.e. return -1
        leftheight = self.findHeight(root.left)
        if leftheight == -1:
            return -1
        #find right height, if -1 terminate early i.e. return -1
        rightheight = self.findHeight(root.right)
        if rightheight == -1:
            return -1
        #if height diff > 1 return -1
        if abs(leftheight - rightheight) > 1:
            return -1
        #return max(leftheight, rightheight) + 1
        return max(leftheight, rightheight) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.findHeight(root)
        return True if height != -1 else False
#TC: O(N) : in each node processing takes O(1) * we traverse all nodes in worst case O(N)
#SC: O(N) : in each node extra space taken is O(1), recursion stack depth is O(d) which is O(log2(n)) for balanced
# O(N) for skewed, take the max

'''
    3
3        5
            7

'''

#ALTERNATE SOLUTIONS:
#WITH dfs post order you can do in two more ways, using a array with 2 values height and balanced,
#  using a class level flag whenever height diff > 1 change the flag
#WITH bfs level order for every node you have to find both childs height, if diff > 1 return -1
        