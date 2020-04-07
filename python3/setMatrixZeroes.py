'''
Problem 73: Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
-A straight forward solution using O(mn) space is probably a bad idea.
-A simple improvement uses O(m + n) space, but still not the best solution.
-Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m: int = len(matrix)
        n: int = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'a'
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'a'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
