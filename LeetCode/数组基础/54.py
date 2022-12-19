from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        array = []
        while True:
            for index in range(left, right + 1):
                array.append(matrix[up][index])
            up += 1
            if up > down:
                break

            for index in range(up, down + 1):
                array.append(matrix[index][right])
            right -= 1
            if right < left:
                break

            for index in range(right, left - 1, -1):
                array.append(matrix[down][index])
            down -= 1
            if down < up:
                break

            for index in range(down, up - 1, -1):
                array.append(matrix[index][left])
            left += 1
            if left > right:
                break
        return array
