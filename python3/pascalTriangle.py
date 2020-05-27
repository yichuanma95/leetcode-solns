'''
Problem 118: Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Solution runtime: 28ms, faster than 93.95% of Python3 solutions
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ''' (Solution, int) -> list of list of int
        
        Returns the first numRows rows of Pascal's Triangle
        
        >>> soln = Solution()
        >>> soln.generate(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        '''
        
        # Base cases
        # Return [] for 0 rows of Pascal's Triangle
        if numRows == 0:
            return []
        
        # Return [[1]] for 1 row (row 0) of Pascal's Triangle
        if numRows == 1:
            return [[1]]
        
        pascals_triangle = [[1], [1, 1]]
        
        # Iteratively generate rows 2-numRows of Pascal's Triangle.
        for r in range(2, numRows):
            # For each new row, start with 1. Then, if the previous row has k elements,
            # then each of the next k - 1 elements is the sum of the consecutive
            # numbers directly above it in the previous row. Finally, finish the new row
            # with one last 1.
            new_row = [1]
            prev_row = pascals_triangle[-1]
            # The previous row has r elements, so no need to call len() on it.
            for i in range(r - 1):
                new_row.append(prev_row[i] + prev_row[i+1])
            new_row.append(1)
            pascals_triangle.append(new_row)
        
        return pascals_triangle
    