'''
Problem 104: Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to
the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ''' (Solution, TreeNode) -> int
        
        Returns the max depth of the binary tree rooted at root by performing a
        post-order traversal on the tree.
        '''
        
        return 0 if root is None else (max(self.maxDepth(root.left),
            self.maxDepth(root.right)) + 1)
    
