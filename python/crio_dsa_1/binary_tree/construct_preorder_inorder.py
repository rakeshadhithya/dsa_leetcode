#LINK: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    #traverses in preorder, take root from preorder array, determine subtrees from inorder array
    def build(self, preorder, in_map, root_index, in_left, in_right):
        if in_left > in_right:
            return None
        root_val = preorder[root_index[0]]
        root = TreeNode(root_val)
        root_index[0] += 1
        position = in_map[root_val]
        root.left = self.build(preorder, in_map, root_index, in_left, position - 1)
        root.right = self.build(preorder, in_map, root_index, position + 1, in_right)
        return root      

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {inorder[i] : i for i in range(len(inorder))}
        return self.build(preorder, in_map, [0], 0, len(inorder) - 1)
    
#TC: O(N) : in_map creation traverses inorder list O(N) + in each node constant time O(1) * total nodes O(N)
#SC: O(N) : in_map stores O(N) + max(in each node new TreeNode created O(1) * total nodes O(N), recursion depth O(N) in worst case)
        


'''
ALTERNATE APPROACH:
logic: prorder: node, leftree, rightree. inorder: leftree, node, rightree. preorder traversal is the only 
way to find root. from preorder array form root, root left(+1), root right(+leftreelength find from inordermap)
def build(self, preorder, in_map, root_index, in_left, in_right):
        root_val = preorder[root_index]
        root = TreeNode(root_val)
        position = in_map[root_val]
        if position > in_left:
            root.left = self.build(preorder, in_map, root_index + 1, in_left, position - 1)
        if position < in_right:
            root.right = self.build(preorder, in_map, root_index + position - in_left + 1, position + 1, in_right)
        return root
'''