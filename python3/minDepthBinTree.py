'''
Problem 111: Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to
the nearest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

Solution runtime: 44ms, faster than 94.23% of Python3 submissions

Solution memory usage: 14.4 MB, less than 91.89% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        ld: int = self.minDepth(root.left)
        rd: int = self.minDepth(root.right)
            
        if root.left is None and root.right is not None:
            ld = float("Inf")
        if root.left is not None and root.right is None:
            rd = float("Inf")

        return min(ld, rd) + 1
