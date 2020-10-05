/*
Problem 107: Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie,
from left to right, level by level from leaf to root).

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

Solution runtime: 4ms, faster than 90.81% of C++ submissions
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> traversalResult;
        if (!root) return traversalResult;
        TreeNode* node;
        vector<int>lvlVals;
        lvlVals.push_back(root->val);
        int currentLv = -1;
        root->val = 0;
        queue<TreeNode*> q;
        q.push(root);
        while(q.size() > 0) {
            node = q.front();
            q.pop();
            if (node->val != currentLv) {
                currentLv = node->val;
                traversalResult.push_back(lvlVals);
                lvlVals.clear();
            }
            if (node->left) {
                lvlVals.push_back(node->left->val);
                node->left->val = currentLv + 1;
                q.push(node->left);
            }
            if (node->right) {
                lvlVals.push_back(node->right->val);
                node->right->val = currentLv + 1;
                q.push(node->right);
            }
        }
        vector<vector<int>> toReturn;
        for (int i = traversalResult.size() - 1; i >= 0; i--) {
            toReturn.push_back(traversalResult[i]);
        }
        return toReturn;
    }
};
