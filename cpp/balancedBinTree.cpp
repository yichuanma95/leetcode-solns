/*
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
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

struct DepthAndBalance {
    int depth;
    bool balanced;
    DepthAndBalance(int d, bool b) {
        depth = d;
        balanced = b;
    };
};

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return traverse(root).balanced;
    }

private:
    DepthAndBalance traverse(TreeNode* node) {
        if (!node) {
            return DepthAndBalance(0, true);
        }
        DepthAndBalance leftResult = traverse(node -> left);
        DepthAndBalance rightResult = traverse(node -> right);
        bool isBalanced = abs(leftResult.depth - rightResult.depth) <= 1;
        return DepthAndBalance(max(leftResult.depth, rightResult.depth) + 1, isBalanced & leftResult.balanced & rightResult.balanced);
    }
};
