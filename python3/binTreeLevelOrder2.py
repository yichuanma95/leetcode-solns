'''
Problem 107: Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from
left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

Solution runtime: 28ms, faster than 99.9% of Python3 submissions

Solution memory usageL 13.1 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        queue: List[TreeNode] = [(root, 1)]
        vals: List[List[int]] = []
        prevLevel: int = 1
        lvNodes = []
        
        while len(queue) > 0:
            node, lv = queue.pop(0)
            if lv != prevLevel:
                vals.insert(0, lvNodes)
                lvNodes = [node.val]
                prevLevel = lv
            else:
                lvNodes.append(node.val)
            
            if node.left is not None:
                queue.append((node.left, lv + 1))
            if node.right is not None:
                queue.append((node.right, lv + 1))
        vals.insert(0, lvNodes)
        
        return vals
