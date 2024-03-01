from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        si = 0
        li = len(nums)-1 #5
        while(si<=li):
            mi = si + (li-si)//2 #2, 4, 5
            if(target == nums[mi]):
                return mi
            elif (target>nums[mi]):
                si = mi+1 #5
            elif (target<nums[mi]):
                li = mi-1
        return -1
