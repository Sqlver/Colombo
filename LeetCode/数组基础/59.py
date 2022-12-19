from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, up, down = 0, n - 1, 0, n - 1
        array = [[0] * n for _ in range(n)]
        count = 1
        while True:
            for index in range(left, right + 1):
                array[up][index] = count
                count += 1
            up += 1
            if up > down:
                break

            for index in range(up, down + 1):
                array[index][right] = count
                count += 1
            right -= 1
            if right < left:
                break

            for index in range(right, left - 1, -1):
                array[down][index] = count
                count += 1
            down -= 1
            if down < up:
                break

            for index in range(down, up - 1, -1):
                array[index][left] = count
                count += 1
            left += 1
            if left > right:
                break
        return array
