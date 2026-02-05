class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            map[nums[i]] = i
        
        for i in range(0, len(nums)):    
            element = target - nums[i]
            if element in map and map[element] != i:
                return [i, map[element]]
        