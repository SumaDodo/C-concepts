# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        curr_node = [root]
        
        while curr_node:
            result.append([node.val for node in curr_node])
            temp = []
            for node in curr_node:
                temp.extend([node.left, node.right])
            curr_node = [leaf for leaf in temp if leaf]
        
        result.reverse()
        return result
