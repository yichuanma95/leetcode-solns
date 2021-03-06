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

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_for_p = []
        self.DFS_and_path_trace(root, p, path_for_p)
        path_for_q = []
        self.DFS_and_path_trace(root, q, path_for_q)
        min_path_length = min(len(path_for_p), len(path_for_q))
        i = 0
        while i < min_path_length - 1 and path_for_p[i] == path_for_q[i]:
            i += 1
        while path_for_p[i] != path_for_q[i]:
            i -= 1
        return TreeNode(path_for_p[i])
    
    def DFS_and_path_trace(self, root, node, path):
        '''
        Performs a depth-first search on the BST rooted at root and traces and records the
        path from root to node.
        '''
        if root is None:
            return
        path.append(root.val)
        self.DFS_and_path_trace(root.left, node, path)
        self.DFS_and_path_trace(root.right, node, path)
        if path[-1] != node.val:
            path.pop()
