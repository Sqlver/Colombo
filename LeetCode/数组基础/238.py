from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_array = n * [0]
        right_array = n * [0]
        answer = n * [0]

        left_array[0] = 1
        for index in range(1, n):
            left_array[index] = left_array[index - 1] * nums[index - 1]

        right_array[-1] = 1
        for index in range(n - 2, -1, -1):
            right_array[index] = right_array[index + 1] * nums[index + 1]

        for index in range(n):
            answer[index] = left_array[index] * right_array[index]

        return answer
