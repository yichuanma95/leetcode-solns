'''
Problem 653: Two Sum IV-Input is a BST

Given the root of a Binary Search Tree and a target number k, return true if there exist
two elements in the BST such that their sum is equal to the given target.

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

Example 3:
Input: root = [2,1,3], k = 4
Output: true

Example 4:
Input: root = [2,1,3], k = 1
Output: false

Example 5:
Input: root = [2,1,3], k = 3
Output: true

Constraints:
* The number of nodes in the tree is in the range [1, 104].
* -104 <= Node.val <= 104
* root is guaranteed to be a valid binary search tree.
* -105 <= k <= 105

Solution runtime: 64ms, faster than 99.3% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        complements = set()
        return self.traverse_for_complements(root, k, complements)
    
    def traverse_for_complements(self, node, k, complements):
        if not node:
            return False
        complement = k - node.val
        if node.val in complements:
            return True
        complements.add(complement)
        return self.traverse_for_complements(node.left, k, complements) or \
            self.traverse_for_complements(node.right, k, complements)
