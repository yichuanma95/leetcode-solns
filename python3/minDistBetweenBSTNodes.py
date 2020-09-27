'''
Problem 783: Minimum Distance Between BST Nodes

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between
the values of any two different nodes in the tree.

Example :
Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.
The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between nodes 1 and 2, and also
between nodes 3 and 2.

Note:
1. The size of the BST will be between 2 and 100.
2. The BST is always valid, each node's value is an integer, and each node's value is different.
3. This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        vals = []
        self.in_order_traverse(root, vals)
        return min(map(lambda x: abs(x[0] - x[1]), list(zip(vals[:-1], vals[1:]))))
        
    def in_order_traverse(self, node, vals):
        if not node:
            return
        self.in_order_traverse(node.left, vals)
        vals.append(node.val)
        self.in_order_traverse(node.right, vals)
