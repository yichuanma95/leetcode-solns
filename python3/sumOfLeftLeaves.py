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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.traverse(root)
        
    def traverse(self, node):
        if node is None:
            return 0
        
        leftLeafSum = 0
        
        if node.left is not None:
            # check if left child is a leaf
            if node.left.left is None and node.left.right is None:
                leftLeafSum = node.left.val
            else:
                leftLeafSum += self.traverse(node.left)
        leftLeafSum += self.traverse(node.right)
        
        return leftLeafSum
