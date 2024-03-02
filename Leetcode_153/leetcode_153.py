from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.calc_min(nums)

    def calc_min(self, nums):
        n=len(nums)
        if (n == 1):
            return nums[0]
        else:
            leftarr = nums[0:n//2]
            rghtarr = nums[n//2:]
            lm = self.calc_min(leftarr)
            rm = self.calc_min(rghtarr)
            return min(lm,rm)
