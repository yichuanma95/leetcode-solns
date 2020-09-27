'''
Problem 543: Diameter Of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of
a binary tree is the length of the longest path between any two nodes in a tree. This path may
or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

Solution runtime: 40ms, faster than 92.45% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_path, diameter = self.traverse_for_diameter(root)
        return diameter
    
    def traverse_for_diameter(self, node) -> (int, int):
        if not node:
            return (0, 0)
        left_path, diameter_left = self.traverse_for_diameter(node.left)
        right_path, diameter_right = self.traverse_for_diameter(node.right)
        return (max(left_path, right_path) + 1, max(diameter_left, diameter_right, left_path + right_path))
    