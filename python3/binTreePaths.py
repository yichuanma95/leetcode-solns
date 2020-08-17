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

Solution runtime: 24ms, faster than 98.2% of Python3 submissions

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.get_root_to_leaf_paths(root, paths)
        return paths
    
    def get_root_to_leaf_paths(self, root, paths, current_path=[]):
        if root is None:
            return
        current_path.append(str(root.val))
        if root.left is None and root.right is None:
            paths.append("->".join(current_path))
        self.get_root_to_leaf_paths(root.left, paths, current_path)
        self.get_root_to_leaf_paths(root.right, paths, current_path)
        current_path.pop()
        