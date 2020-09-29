/*
Problem 21: Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* current1 = l1, *current2 = l2;
        ListNode* prev1 = NULL, *prev2 = NULL;
        ListNode* headOfMerged = NULL, *endOfMerged = NULL;
        vector<ListNode*> headAndLast;
        while (current1 && current2) {
            if (current1->val <= current2->val) {
                prev1 = current1;
                current1 = current1->next;
                prev1->next = NULL;
                headAndLast = insertAtEnd(headOfMerged, endOfMerged, prev1);
            } else {
                prev2 = current2;
                current2 = current2->next;
                prev2->next = NULL;
                headAndLast = insertAtEnd(headOfMerged, endOfMerged, prev2);
            }
            headOfMerged = headAndLast[0];
            endOfMerged = headAndLast[1];
        }
        if (current1) {
            headAndLast = insertAtEnd(headOfMerged, endOfMerged, current1);
            headOfMerged = headAndLast[0];
            endOfMerged = headAndLast[1];
        }
        if (current2) {
            headAndLast = insertAtEnd(headOfMerged, endOfMerged, current2);
            headOfMerged = headAndLast[0];
            endOfMerged = headAndLast[1];
        }
        return headOfMerged;
    }
    
private:
    vector<ListNode*> insertAtEnd(ListNode* head, ListNode* lastElem, ListNode* node) {
        if (!lastElem) {
            lastElem = node;
            head = node;
        } else {
            lastElem->next = node;
            lastElem = lastElem->next;
        }
        vector<ListNode*> result;
        result.push_back(head);
        result.push_back(lastElem);
        return result;
    }
};
