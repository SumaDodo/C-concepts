# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Using Stack
        
        stack = []
        depth = 0
        
        if root is not None:
            stack.append((1,root))
            
        while stack != []:
            current_depth, node = stack.pop()
            if node is not None:
                depth = max(current_depth, depth)
                stack.append((current_depth+1, node.left))
                stack.append((current_depth+1, node.right))
                
        return depth
