from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        left_sum = 0
        for index, value in enumerate(nums):
            if (2 * left_sum + value) == all_sum:
                return index
            left_sum += value
        return -1
