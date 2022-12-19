from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        x, y = 0, 0
        array = []
        for index in range(m * n):
            array.append(mat[x][y])
            if (x + y) % 2 == 0:
                if y == n - 1:
                    x += 1
                elif x == 0:
                    y += 1
                else:
                    y += 1
                    x -= 1
            else:
                if x == m - 1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1
        return array
