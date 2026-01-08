class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        delete_zeros = 0
        max_count = 0
        count_ones = 0
        i,j = 0,0
        for j in range (0, n):
            if nums[j] == 0:
                delete_zeros += 1
                while delete_zeros > 1:
                    if nums[i] == 0:
                        delete_zeros -= 1
                    i += 1
            count_ones = j-i
            max_count = max(max_count, count_ones)

        return max_count