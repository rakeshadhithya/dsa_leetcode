#LINK: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def findInorder(self, root, list):
        #if null return
        if root == None:
            return
        #traverse left
        self.findInorder(root.left, list)
        #add current
        list.append(root.val)
        #traverse right
        self.findInorder(root.right, list)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = list()
        self.findInorder(root, ans)
        return ans
    
#TC: O(N), each node processing takes O(1) and total nodes O(N)
#SC: O(N), each node adds a element to list, total nodes O(N) + plus recursion stack depth: 
#           log2(totalNodes(N)) in best(balanced), O(N) in worst(skewed tree)max O(N), 2N -> N

'''
  1
     2
  3

null- return
[1]
null -return
[1, 3]
null - return
[1, 3, 2]
null - return 
'''