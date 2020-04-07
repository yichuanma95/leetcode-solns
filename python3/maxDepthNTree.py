'''
Problem 559: Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to
the farthest leaf node.

For example, given a 3-ary tree:
1
|-3
| |-5
| |-6
|-2
|-4
* my best recreation of an N-ary tree with ASCII in a Python comment

We should return its max depth, which is 3.

Note:
1. The depth of the tree is at most 1000.
2. The total number of nodes is at most 5000.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.postOrder(root)
    
    def postOrder(self, node: 'Node') -> int:
        if node is None:
            return 0
        if len(node.children) == 0:
            return 1
        
        depths: List[int] = [self.postOrder(child) for child in node.children]
        
        return max(depths) + 1
