from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        si=0
        li=n-1
        while(si<=li):
            mi = si + (li-si)//2
            if(target == nums[mi]):
                return mi

            if(nums[mi]>=nums[si]):
                if(target>nums[mi] or target<nums[si]):
                    si = mi+1
                else:
                    li=mi-1
            else:
                if (target>nums[li] or target<nums[mi]):
                    li = mi-1
                else:
                    si = mi+1
        return -1
