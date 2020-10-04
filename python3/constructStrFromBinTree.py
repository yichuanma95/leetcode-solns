'''
Problem 606: Construct String from Binary Tree

You need to construct a string consists of parenthesis and integers from a binary tree with
the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all
the empty parenthesis pairs that don't affect the one-to-one mapping relationship between
the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"
Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        val_chars = []
        self.traverse_and_build_str(t, val_chars)
        return ''.join(val_chars)
    
    def traverse_and_build_str(self, node, val_chars):
        if not node:
            return
        val_chars.append(str(node.val))
        if not (node.left or node.right):
            return
        val_chars.append('(')
        self.traverse_and_build_str(node.left, val_chars)
        val_chars.append(')')
        if not node.right:
            return
        val_chars.append('(')
        self.traverse_and_build_str(node.right, val_chars)
        val_chars.append(')')
        