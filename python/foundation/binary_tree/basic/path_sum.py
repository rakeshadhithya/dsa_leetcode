#LINK: https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def findPathSum(self, root, total, targetSum):
        #if root is None then no path sum
        if root == None:
            return False
        #add root val to total
        total += root.val
        #if root if leaf, return if total == targetSum
        if root.left == None and root.right == None:
            return total == targetSum
        #find left, if found return true
        leftsub = self.findPathSum(root.left, total, targetSum)
        if leftsub:
            return True
        #find right, if found return true
        rightsub = self.findPathSum(root.right, total, targetSum)
        if rightsub:
            return True
        #return False
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.findPathSum(root, 0, targetSum)

#TC: O(N) : in each node time taken is O(1) * total nodes in worst case is O(N)
#SC: O(N) : in each node extra space taken is O(1) (no auxilary data structures), recursion stack depth is 
# O(N) for skewed O(log2(N)) for balanced, take max one don't add



#ALTERNATE SOLUTIONS
#in dfs preorder instead of adding node value you can also subtract and send reduced sum to childs
#BFS level order. create a custom class for each node - NodePair which has node, and sum up to that node. 
# if node is leaf and sum is target return True else if none found return False