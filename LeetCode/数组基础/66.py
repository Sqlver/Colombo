from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for index in range(n - 1, -1, -1):
            if digits[index] == 9:
                digits[index] = 0
                continue
            digits[index] += 1
            return digits
        return [1] + [0] * n
