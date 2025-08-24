# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#USING DFS PREORDER
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        #add each node value including none, as strs
        code = []
        self.serializer(root, code)
        return ','.join(code)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        #add each value from str code to queue
        dq = deque()
        dq.extend(data.split(','))
        return self.deserializer(dq)


    #append each value in preorder to code list
    def serializer(self, root, code):
        if root == None:
            code.append('none')
            return
        code.append(str(root.val))
        self.serializer(root.left, code)
        self.serializer(root.right, code)

    #deque each value and create root(whole tree)
    def deserializer(self, dq):
        if len(dq) == 0:
            return None
        node_val = dq.popleft()
        if node_val =='none':
            return
        root = TreeNode(int(node_val))
        root.left = self.deserializer(dq)
        root.right = self.deserializer(dq)
        return root
    
#TC: O(N) : serialize: serializer func takes O(N) to traverse and append, then join takes O(N) to traverse the code str
#           desrialize: extend takes O(N) to traverse each element in code str, deserializer func traverse each appended node in dequeue O(N)
#                       O(2N) for serialze, O(2N) for deserialize -> O(N)
#SC: O(N) : serialize: code list takes O(N), then join takes O(N). recursion stack in worst case O(N)
#           deserialize: dq takes O(N), split function return O(N) list, then deserializer create O(N) nodes.
#                        then recursion stack takes O(N) in worst case. max of all is O(N)
        
'''
      3
   5     4

3, 5, 4,

'''

#ALTERNATE APPROACH: BFS (LATER)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))