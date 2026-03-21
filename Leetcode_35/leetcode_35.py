class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start = 0
        end = length-1
        mid = length//2

        while start<=end and start<length and end>-1:
            mid = (end+start+1)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                start = mid+1
            elif target<nums[mid]:
                end = mid-1
        if target<nums[mid]:
            return mid
        return mid+1