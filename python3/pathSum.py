'''
Problem 112: Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding
up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Solution runtime: 44ms, faster than 95.06% of Python3 submissions

Solution memory usage: 14.4 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.helper(root, sum, 0)
    
    def helper(self, node: TreeNode, sum: int, soFar: int) -> bool:
        if node is None:
            return False
        
        soFar += node.val
        if soFar == sum and node.left is None and node.right is None:
            return True
        
        return self.helper(node.left, sum, soFar) or self.helper(node.right, sum, soFar)
