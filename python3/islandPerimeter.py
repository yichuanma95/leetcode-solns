'''
Problem 463: Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and
0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the
island). One cell is a square with side length 1. The grid is rectangular, width and height
don't exceed 100. Determine the perimeter of the island.

Example:
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
Image for explanation is actually on LeetCode.
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 4 * sum(sum(row) for row in grid)
        for i, row in enumerate(grid):
            perimeter -= self.process_row(grid, i, row)
        return perimeter
    
    def process_row(self, grid, i, row):
        to_subtract = 0
        for j, v in enumerate(row):
            if v == 1:
                to_subtract += self.check_neighbor(grid, (i - 1, j))
                to_subtract += self.check_neighbor(grid, (i, j + 1))
                to_subtract += self.check_neighbor(grid, (i + 1, j))
                to_subtract += self.check_neighbor(grid, (i, j - 1))
        return to_subtract

    def check_neighbor(self, grid, neighbor):
        i, j = neighbor
        if i < 0 or j < 0:
            return 0
        try:
            return grid[i][j]
        except IndexError:
            return 0
