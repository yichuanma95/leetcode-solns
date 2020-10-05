/*
Problem 111: Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to
the nearest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.
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

class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        int leftDepth = minDepth(root->left);
        int rightDepth = minDepth(root->right);
        if (leftDepth == 0 && rightDepth == 0) return 1;
        if (leftDepth != 0 && rightDepth == 0) return leftDepth + 1;
        if (leftDepth == 0 && rightDepth != 0) return rightDepth + 1;
        return min(leftDepth, rightDepth) + 1;
    }
};
