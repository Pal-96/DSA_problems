class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * n
        p[0] = nums[0]
        for i in range(1, n):
            p[i] = p[i-1] + nums[i]
        for i in range(0,n):
            if i == 0:
                if p[n-1] - p[i] == 0:
                    return i
                continue
            if p[n-1] - p[i] == p[i-1]:
                return i
        return -1