class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_area=float('-inf')
        while l< r:
                max_area = max(max_area, min(height[l], height[r]) * (r-l))
                if height[r]>height[l]:
                    l+=1
                    continue
                r-=1        
        return max_area