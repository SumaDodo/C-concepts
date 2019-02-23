# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.result = []
        def serial(node):
            if node:
                self.result.append(str(node.val))
                serial(node.left)
                serial(node.right)
            else:
                self.result.append("null")
        serial(root)
        return ' '.join(self.result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def deserial(values):
            val = next(values)
            if val == 'null':
                return None
            else:
                node = TreeNode(int(val))
                node.left = deserial(values)
                node.right = deserial(values)
            return node
        values = iter(data.split())
        return deserial(values)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
