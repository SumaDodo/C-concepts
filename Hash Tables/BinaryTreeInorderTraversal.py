# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        values = []
        
        if root == None:
            return []
        
        stack.append(root)
        while(len(stack)!=0):
            while root!= None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            values.append(root.val)
            root = root.right
            
        return values[:-1]
