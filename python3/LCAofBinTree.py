'''
Problem 236: Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself).”

Given the following binary tree: root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Notes:
-All of the nodes' values will be unique.
-p and q are different and both values will exist in the binary tree.

Solution memory usage: 23.2 MB, less than 91.67% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = []
        
        self.traverse(root, p, q, [], paths)
        pathP = paths[0]
        pathQ = paths[1]
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i] != pathQ[i]:
                return TreeNode(pathP[i-1])
            
        if len(pathP) > len(pathQ):
            return TreeNode(pathQ[-1])
        return TreeNode(pathP[-1])
        
    def traverse(self, node, p, q, path, collector):
        if node is None:
            return
        
        path.append(node.val)
        if node.val in [p.val, q.val]:
            collector.append(copy.deepcopy(path))
        if len(collector) == 2:
            return
        self.traverse(node.left, p, q, path, collector)
        self.traverse(node.right, p, q, path, collector)
        path.pop()
