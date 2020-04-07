'''
Problem 257: Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3

Solution runtime: 24ms, faster than 95.03% of Python3 submissions

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        
        self.traverse(root, [], paths)
        
        return paths
    
    def traverse(self, node, path, collector):
        if node is None:
            return
        
        path.append(str(node.val))
        if node.left is None and node.right is None:
            collector.append('->'.join(path))
        self.traverse(node.left, path, collector)
        self.traverse(node.right, path, collector)
        path.pop()
