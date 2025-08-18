#LINK: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return list()
        #take anslist, queue, add root
        ans = []
        queue = Queue()
        queue.put(root)
        #until queue empty
        while not queue.empty():
            #take currsize and currlist
            currsize = queue.qsize()
            currlist = []
            #for currsize times
            for i in range(currsize):
                #pop and process root(add val to currlist)
                node = queue.get()
                currlist.append(node.val)
                #if not null add left child to queue
                if node.left:
                    queue.put(node.left)
                #if not null add right child to queue
                if node.right:
                    queue.put(node.right)
            #add currlist to main list
            ans.append(currlist)
        return ans