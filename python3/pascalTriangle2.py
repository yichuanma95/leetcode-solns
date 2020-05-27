'''
Problem 119: Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Follow up: Could you optimize your algorithm to use only O(k) extra space?

Solution runtime: 24ms, faster than 92.64% of Python3 submissions
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ''' (Solution, int) -> list of int
        
        Returns the row of Pascal's triangle at index rowIndex. Row indices of
        Pascal's triangle are zero-based.
        
        >>> soln = Solution()
        >>> soln.getRow(3)
        [1, 3, 3, 1]
        '''
        
        # Base case
        # First row (at index 0) is [1]
        if rowIndex == 0:
            return [1]
        
        # Second row is [1, 1]
        prev_row = [1, 1]
        
        # Iteratively find the row at rowIndex.
        # Use the values in the previous row to generate the next row.
        for r in range(1, rowIndex):
            new_row = [1]
            # The previous row will have r + 1 elements in it.
            for i in range(r):
                new_row.append(prev_row[i] + prev_row[i+1])
            new_row.append(1)
            prev_row = new_row
        
        return prev_row

