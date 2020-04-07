'''
Problem 653: Two Sum IV-Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the
BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True

Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
Output: False
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        self.inOrderMakeSet(root, s)
        
        while len(s) > 0:
            e = s.pop()
            if (k - e) in s:
                return True
        
        return False
        
    def inOrderMakeSet(self, node: TreeNode, s):
        if node is None:
            return
        self.inOrderMakeSet(node.left, s)
        s.add(node.val)
        self.inOrderMakeSet(node.right, s)
