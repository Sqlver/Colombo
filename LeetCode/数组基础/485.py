from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_consecutive = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > max_consecutive:
                    max_consecutive = count
            else:
                count = 0
        return max_consecutive
