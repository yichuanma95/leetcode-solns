'''
Problem 637: Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form
of an array.

Example:
Input:
    3
   / \
  9  20
    /  \
   15   7

Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence
return [3, 14.5, 11].

Note: The range of node's value is in the range of 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level_to_values = defaultdict(list)
        self.traverse_and_gather(root, level_to_values, 0)
        return list(map(lambda x: sum(x) / len(x), level_to_values.values()))
    
    def traverse_and_gather(self, node, level_to_values, depth):
        if not node:
            return
        level_to_values[depth].append(node.val)
        self.traverse_and_gather(node.left, level_to_values, depth + 1)
        self.traverse_and_gather(node.right, level_to_values, depth + 1)
    