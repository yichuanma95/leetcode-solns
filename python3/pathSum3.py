'''
Problem 437: Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

Solution memory usage: 13.6 MB, less than 90.91% of Python3 submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.preOrder(root, sum, [])
    
    def preOrder(self, node: TreeNode, sum: int, sums: List[int]) -> int:
        if node is None:
            return 0
        
        count: int = 0
        val: int = node.val
            
        for i in range(len(sums)):
            sums[i] += val
        sums.append(val)
        for s in sums:
            if s == sum:
                count += 1
        count += self.preOrder(node.left, sum, sums)
        count += self.preOrder(node.right, sum, sums)
        for i in range(len(sums)):
            sums[i] -= val
        sums.pop()
        
        return count
