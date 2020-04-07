'''
Problem 110: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as: a binary tree in which the left
and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.

Solution runtime: 52ms, faster than 94.61% of Python3 submissions

Solution memory usage: 16.3 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        self.traverse(root)
        
        return root.val
    
    # post-order tree traversal
    def traverse(self, node: TreeNode) -> int:
        if node is None:
            return 0
        
        ld: int = self.traverse(node.left)
        rd: int = self.traverse(node.right)
        
        node.val = abs(ld - rd) <= 1
        if node.left is not None and node.right is not None:
            node.val = node.val and (node.left.val and node.right.val)
        
        return max(ld, rd) + 1
