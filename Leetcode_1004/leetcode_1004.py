class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_length = float('-inf')
        w_len = 0
        num_zeros = 0
        i, j = 0,0
        for j in range (0, n):
            if nums[j] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[i] == 0:
                    num_zeros -= 1
                i += 1
            
            w_len = j - i + 1
            max_length =max(max_length, w_len)
        
        return max_length
            

        