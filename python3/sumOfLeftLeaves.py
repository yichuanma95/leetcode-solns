'''
Problem 404: Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

Solution memory usage: 13 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        vals = []
        self.get_left_leaf_vals(root, vals)
        return sum(vals)
    
    def get_left_leaf_vals(self, root, vals):
        if not root:
            return
        self.get_left_leaf_vals(root.left, vals)
        if root.left and not (root.left.left or root.left.right):
            vals.append(root.left.val)
        self.get_left_leaf_vals(root.right, vals)
