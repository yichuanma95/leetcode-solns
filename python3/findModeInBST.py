'''
Problem 501: Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently
occurred element) in the given BST.

Assume a BST is defined as follows:
-The left subtree of a node contains only nodes with keys less than or equal to the node's key.
-The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
-Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack
space incurred due to recursion does not count).

Solution memory usage: 16.6 MB, less than 100% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        essentials = [0,0]
        # 1st value is current streak, 2nd value is max streak, 3rd value is previous value
        modes = []
        
        self.inOrder(root, essentials, modes)
        if essentials[0] > essentials[1]:
            return [essentials[2]]
        elif essentials[0] == essentials[1]:
            modes.append(essentials[2])
        
        return modes
    
    def inOrder(self, node, essentials, modes):
        if node is None:
            return
        
        self.inOrder(node.left, essentials, modes)
        if len(essentials) == 2:
            essentials.append(node.val)
            essentials[0] = 1
            modes.append(node.val)
        else:
            if node.val == essentials[2]:
                essentials[0] += 1
            else:
                if essentials[0] > essentials[1]:
                    essentials[1] = essentials[0]
                    while len(modes) > 1:
                        modes.pop()
                    modes[0] = essentials[2]
                elif essentials[0] == essentials[1]:
                    modes.append(essentials[2])
                essentials[0] = 1
                essentials[2] = node.val
        self.inOrder(node.right, essentials, modes)
