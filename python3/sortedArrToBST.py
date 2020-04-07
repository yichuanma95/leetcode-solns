'''
Problem 108: Convbert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Solution runtime: 64ms, faster than 99.38% of Python3 submissions

Solution memory usage: 14.9 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.binSearch(nums, 0, len(nums) - 1)
    
    def binSearch(self, nums, lo, hi) -> TreeNode:
        if lo > hi:
            return None
        
        mid: int = (lo + hi) // 2
        node: TreeNode = TreeNode(nums[mid])
        node.left = self.binSearch(nums, lo, mid - 1)
        node.right = self.binSearch(nums, mid + 1, hi)
        
        return node
