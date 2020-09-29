'''
Problem 572: Subtree of Another Subtree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all
of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s. 

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2

Return false.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.verify_subtree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def verify_subtree(self, s, t):
        if not s and not t:
            return True
        if not s and t or s and not t:
            return False
        if s.val != t.val:
            return False
        return self.verify_subtree(s.left, t.left) and self.verify_subtree(s.right, t.right)
    