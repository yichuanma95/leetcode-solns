'''
Problem 501: Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently
occurred element) in the given BST.

Assume a BST is defined as follows:
-The left subtree of a node contains only nodes with keys less than or equal to the node's key.
-The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
-Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack
space incurred due to recursion does not count).

Solution memory usage: 16.6 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        elem_freq = defaultdict(int)
        self.traverse_for_mode(root, elem_freq)
        frequencies = list(elem_freq.items())
        frequencies.sort(key=lambda x: x[1], reverse=True)
        result = []
        try:
            max_freq = frequencies[0][1]
        except IndexError:
            return result
        i = 0
        while i < len(frequencies) and frequencies[i][1] == max_freq:
            result.append(frequencies[i][0])
            i += 1
        return result
        
    def traverse_for_mode(self, node, elem_freq):
        if not node:
            return
        self.traverse_for_mode(node.left, elem_freq)
        elem_freq[node.val] += 1
        self.traverse_for_mode(node.right, elem_freq)
