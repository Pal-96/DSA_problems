class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alt = 0
        max_alt = 0
        for i in gain:
            cur_alt = cur_alt + i
            max_alt = max(cur_alt, max_alt)
        return max_alt