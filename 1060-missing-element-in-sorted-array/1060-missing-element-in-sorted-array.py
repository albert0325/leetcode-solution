from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = right - (right - left) // 2
            if nums[mid] - nums[0] - mid < k:
                left = mid
            else:
                right = mid - 1
        return nums[0] + k + left