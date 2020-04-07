'''
Problem 289: Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a
cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each
cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following
four rules (taken from the above Wikipedia article):
    1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population..
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current
state. The next state is created by applying the above rules simultaneously to every cell in
the current state, where births and deaths occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
1. Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is
infinite, which would cause problems when the active area encroaches the border of the array.
How would you address these problems?
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m: int = len(board)
        n: int = len(board[0])

        for i in range(m):
            for j in range(n):
                # count live neighbours
                neighbours: int = self.countNeighbours(board, i, j)
                
                # update cells according to the rules
                if board[i][j] == 1:
                    if neighbours < 2 or neighbours > 3:
                        board[i][j] = -1
                else:
                    if neighbours == 3:
                        board[i][j] = 2
        
        # fix the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0

    def countNeighbours(self, board: List[List[int]], i: int, j: int) -> None:
        count: int = 0
        
        for k in range(j - 1, j + 2):
            try:
                if i > 0 and k >= 0:
                    if board[i - 1][k] in (1, -1):
                        count += 1
            except IndexError:
                pass
            try:
                if k >= 0:
                    if board[i + 1][k] in (1, -1):
                        count += 1
            except IndexError:
                pass
        if j > 0:
            if board[i][j - 1] in (1, -1):
                count += 1
        try:
            if board[i][j + 1] in (1, -1):
                count += 1
        except IndexError:
            pass
        
        return count
