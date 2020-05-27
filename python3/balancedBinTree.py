'''
Problem 110: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as: a binary tree in which the left
and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.

Solution runtime: 44ms, faster than 94.73% of Python3 submissions

Solution memory usage: 16.3 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ''' (Solution, TreeNode) -> bool
        
        Returns True if the binary tree rooted at root is height-balanced.
        '''
        return self.traverse(root)[1]
    
    def traverse(self, root):
        ''' (Solution, TreeNode) -> (int, bool)
        
        Performs a post-order traversal on the binary tree rooted at root to see if
        it's height-balanced. Returns a tuple containing the tree's maximum depth and
        a Boolean indicating whether the tree is balanced or not.
        '''
        if root is None:
            return (0, True)
        
        left_depth, is_left_balanced = self.traverse(root.left)
        right_depth, is_right_balanced = self.traverse(root.right)
        is_balanced_overall = abs(left_depth - right_depth) <= 1

        return (max(left_depth, right_depth) + 1,
            is_balanced_overall and is_left_balanced and is_right_balanced)
    