'''
Problem 563: Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left
subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3

Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

Notes:
1. The sum of node values in any subtree won't exceed the range of 32-bit integer.
2. All the tilt values won't exceed the range of 32-bit integer.

Solution runtime: 52ms, faster than 93.06% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total_sum, tilt = self.sum_and_tilt(root)
        return tilt
    
    def sum_and_tilt(self, node) -> (int, int):
        if not node:
            return (0, 0)
        left_sum, left_tilt = self.sum_and_tilt(node.left)
        right_sum, right_tilt = self.sum_and_tilt(node.right)
        tilt = left_tilt + right_tilt + abs(left_sum - right_sum)
        return (left_sum + right_sum + node.val, tilt)
    