from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = self.return_peak(nums)
        return nums.index(peak)

    def return_peak(self, nums: List[int]):
        n=len(nums)
        if n==1:
            return nums[0]
        else:
            lftarr=nums[0:n//2]
            rghtarr=nums[n//2:]
            leftmax = self.return_peak(lftarr)
            rghtmax = self.return_peak(rghtarr)
            return max(leftmax,rghtmax)
