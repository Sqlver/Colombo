from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        m, n = len(board), len(board[0])

        for row in range(m):
            for col in range(n):
                lives = 0
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if 0 <= new_row < m and 0 <= new_col < n and abs(board[new_row][new_col]) == 1:
                        lives += 1
                if board[row][col] == 0 and lives == 3:
                    board[row][col] = 2
                if board[row][col] == 1 and (lives < 2 or lives > 3):
                    board[row][col] = -1

        for row in range(m):
            for col in range(n):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == -1:
                    board[row][col] = 0
