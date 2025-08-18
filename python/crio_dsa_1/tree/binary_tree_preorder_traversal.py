#LINK: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def findPreorder(self, root, list):
        #if root None return
        if root == None:
            return
        #add root val
        list.append(root.val)
        #traverse left
        self.findPreorder(root.left, list)
        #traverse right
        self.findPreorder(root.right, list)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.findPreorder(root, ans)
        return ans
#TC: O(N), each node processing takes O(1) and total nodes O(N)
#SC: O(N), each node adds a element to list, total nodes O(N) + plus recursion stack depth: 
#           log2(totalNodes(N)) in best(balanced), O(N) in worst(skewed tree)max O(N), 2N -> N

'''
   1
      2
    3
[1]
None - return
[1, 2]
[1, 2, 3]
None - return
None - return 
None - return 
'''
        