'''
Problem 671: Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where
each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then
this node's value is the smaller value among its two sub-nodes. More formally, the
property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all
the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        non_min_vals = []
        self.traverse_and_gather_vals(root, root.val, non_min_vals)
        return -1 if len(non_min_vals) == 0 else min(non_min_vals)
    
    def traverse_and_gather_vals(self, node, root_val, non_min_vals):
        if not node:
            return
        if node.val > root_val:
            non_min_vals.append(node.val)
        self.traverse_and_gather_vals(node.left, root_val, non_min_vals)
        self.traverse_and_gather_vals(node.right, root_val, non_min_vals)
        