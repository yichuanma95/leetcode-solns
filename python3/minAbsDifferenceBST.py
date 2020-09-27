'''
Problem 530: Minimum Absolute Difference in BST

Given a binary search tree with non-negative values, find the minimum absolute difference
between values of any two nodes.

Example:
Input:
   1
    \
     3
    /
   2

Output: 1
Explanation: The minimum absolute difference is 1, which is the difference between 2 and 1
(or between 2 and 3). 

Notes:
-There are at least two nodes in this BST.
-This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        vals = []
        self.in_order_traverse(root, vals)
        return min(map(lambda x: abs(x[0] - x[1]), list(zip(vals[:-1], vals[1:]))))
        
    def in_order_traverse(self, node, vals):
        if not node:
            return
        self.in_order_traverse(node.left, vals)
        vals.append(node.val)
        self.in_order_traverse(node.right, vals)
