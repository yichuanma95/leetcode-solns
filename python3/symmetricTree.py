'''
Problem 101: Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
 

Note: Bonus points if you could solve it both recursively and iteratively.

Solution runtime: 32ms, faster than 98.73% of Python3 submissions

Solution memory usage: 12.8 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p.val != q.val:
            return False
        
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
