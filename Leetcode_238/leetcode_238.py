from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        p1,p2 = 1,1

        for i in range(n):
            if i==0:
                ans[i] = 1
            else:
                v1 = nums[i-1]
                p1 = p1 * v1
                ans[i] = p1

        for i in range(n):
            if i == 0:
                ans[n-1] = ans[n-1] * 1
            else:
                v2 = nums[n-i]
                p2 = p2 * v2
                ans[n-i-1] = p2 * ans[n-i-1]

        return ans
