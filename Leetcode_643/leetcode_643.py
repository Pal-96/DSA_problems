class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = 0
        max_avg = float('-inf')

        for i in range(0, k):
            cur_sum += nums[i]
        avg = cur_sum/k
        max_avg = max(max_avg, avg)

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            avg = cur_sum/k
            max_avg = max(max_avg, avg)

        return max_avg
        
