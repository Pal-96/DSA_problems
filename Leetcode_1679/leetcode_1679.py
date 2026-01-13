class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = nums.sort()
        i=0
        j=len(nums)-1
        op=0
        while i<j:
            if sorted_nums[i] + sorted_nums[j] == k:
                op+=1
                i+=1
                j-=1
            if sorted_nums[i] + sorted_nums[j]>k:
                j-=1
            if sorted_nums[i] + sorted_nums[j]<k:
                i+=1
        return op
        # op = 0
        # l,r = 0,1
        # while l<r and l<len(nums)-1:
        #     if len(nums) == 0:
        #         break
        #     if r == len(nums):
        #         l+=1
        #         r = l+1
        #     if nums[l]>=k:
        #         nums.pop(l)
        #         continue
        #     # print(nums[l])
        #     # print(nums[r])
        #     # print(nums)
        #     if r<len(nums) and nums[l]+nums[r]==k:
        #         nums.pop(l)
        #         nums.pop(r-1)
        #         op+=1
        #         l,r = 0,1
        #         continue
        #         # l+=1
        #     r+=1
        
            
