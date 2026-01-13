class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range (0, len(nums)):
            if nums[r]:
                nums[r], nums[l] = nums[l] , nums[r]
                l+=1
            
        # size = len(nums)
        # temp = deque()
        # for i in range(0, size):
        #     if nums[i] == 0:
        #         temp.append(nums[i])
        #         continue
        #         # print (temp)
        #     temp.appendleft(nums[i])
        # ctr,i = 0,0
        # for j in range(size-1, -1, -1):
        #     get_item = temp.pop()
        #     if get_item == 0:
        #         nums[j] = get_item
        #         continue
        #     nums[i] = get_item
        #     i+=1