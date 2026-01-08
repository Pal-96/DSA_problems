class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        arr = list(s)
        count = 0
        vowels = set(('a', 'e', 'i', 'o', 'u'))
        max_count = float('-inf')
        for i in range (0,k):
            if arr[i] in vowels:
                count+=1
            max_count = max(max_count, count)

        for i in range (k, n):
            if arr[i-k] in vowels:
                count -= 1
            
            if arr[i] in vowels:
                count += 1

            max_count = max(max_count, count)
        
        return max_count