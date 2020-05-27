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

Solution runtime: 40ms, faster than 94.23% of Python3 submissions

Solution memory usage: 14.4 MB, less than 91.89% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        ''' (Solution, TreeNode) -> int
        
        Return the number of nodes along the shortest path from the root to the nearest
        leaf. This method performs a post-order traversal to calculate this number.
        '''
        
        if root is None:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        # current node is a leaf
        if left_depth == 0 and right_depth == 0:
            return 1
        # if current node only has a left child, consider only depth of left child
        if left_depth != 0 and right_depth == 0:
            return left_depth + 1
        # if current node only has a right child, consider only depth of right child
        if left_depth == 0 and right_depth != 0:
            return right_depth + 1
        
        return min(left_depth, right_depth) + 1
    