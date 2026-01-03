class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        arr = list(s)
        count = 0
        max_count = float('-inf')
        for i in range (0,k):
            if arr[i] in ('a', 'e', 'i', 'o', 'u'):
                count+=1
            max_count = max(max_count, count)

        for i in range (k, n):
            if arr[i-k] in ('a', 'e', 'i', 'o', 'u'):
                count -= 1
            
            if arr[i] in ('a', 'e', 'i', 'o', 'u'):
                count += 1

            max_count = max(max_count, count)
        
        return max_count
                
        