'''
Problem 119: Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Follow up: Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prevRow: List[int] = [1, 1]
            
        if rowIndex == 1:
            return prevRow
        
        for i in range(rowIndex - 1):
            row = [1]
            for j in range(1, len(prevRow)):
                row.append(prevRow[j] + prevRow[j - 1])
            row.append(1)
            prevRow = row
            
        return prevRow
