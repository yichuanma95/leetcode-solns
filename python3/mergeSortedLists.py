'''
Problem 21: Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' (Solution, ListNode, ListNode) -> ListNode
        
        Given two linked lists whose elements are in sorted order, return a new merged
        linked list containing elements of both lists in sorted order
        '''
        
        current1 = l1
        current2 = l2
        prev1 = None
        prev2 = None
        head_of_merged = None
        end_of_merged = None
        
        while current1 is not None and current2 is not None:
            if current1.val <= current2.val:
                prev1 = current1
                current1 = current1.next
                prev1.next = None
                head_of_merged, end_of_merged = self.insert_at_end(head_of_merged, end_of_merged, prev1)
            else:
                prev2 = current2
                current2 = current2.next
                prev2.next = None
                head_of_merged, end_of_merged = self.insert_at_end(head_of_merged, end_of_merged, prev2)
        
        if current1 is not None:
            head_of_merged, end_of_merged = self.insert_at_end(head_of_merged, end_of_merged, current1)
        if current2 is not None:
            head_of_merged, end_of_merged = self.insert_at_end(head_of_merged, end_of_merged, current2)
        
        return head_of_merged

    def insert_at_end(self, head: ListNode, last_elem: ListNode, node: ListNode) -> ListNode:
        ''' (Solution, ListNode, int) -> ListNode
        
        Insert node at the end of a linked list whose head is head and last element
        is last_elem. If the list was originally empty, make head point to the newly
        inserted node. Otherwise, once node is inserted, move last_elem pointer to the newly
        inserted node, which is the new last element in the list.     
        '''
        
        if last_elem is None:
            last_elem = node
            head = node
        else:
            last_elem.next = node
            last_elem = last_elem.next

        return (head, last_elem)
