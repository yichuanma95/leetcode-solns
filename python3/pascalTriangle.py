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

Solution runtime: 32ms, faster than 93.95% of Python3 solutions
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        triangle: List[List[int]] = [[1], [1,1]]
        
        if numRows == 2:
            return triangle
        
        for i in range(numRows - 2):
            lastRow: List[int] = triangle[-1]
            nextRow: List[int] = [1]
            for j in range(1, len(lastRow)):
                nextRow.append(lastRow[j] + lastRow[j - 1])
            nextRow.append(1)
            triangle.append(nextRow)
        
        return triangle
