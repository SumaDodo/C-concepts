# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start>end:
                return [None,]
            
            tree_list = []
            for i in range(start, end+1):
                left_subtree = generate_trees(start, i-1)
                right_subtree = generate_trees(i+1, end)
                
                for l in left_subtree:
                    for r in right_subtree:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        tree_list.append(current_tree)
                        
            return tree_list
        
        return generate_trees(1, n) if n else []
