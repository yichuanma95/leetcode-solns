'''
Problem 687: Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the
same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more
than 1000.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = [0]
        self.arrow_length(root, ans)
        return ans[0]
    
    def arrow_length(self, node, ans):
        if not node:
            return 0
        left_length = self.arrow_length(node.left, ans)
        right_length = self.arrow_length(node.right, ans)
        left_arrow = 0
        right_arrow = 0
        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1
        ans[0] = max(ans[0], left_arrow + right_arrow)
        return max(left_arrow, right_arrow)
