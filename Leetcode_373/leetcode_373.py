import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minarr = []
        visited = set()
        n = len(nums1)
        m = len(nums2)
        ans = []
        heapq.heappush(minarr, [nums1[0]+nums2[0],0,0])
        for _ in range(min(k, (m*n))):
            sum, i,j = heapq.heappop(minarr)
            ans.append([nums1[i], nums2[j]])
            if i+1<n and (i+1,j) not in visited:
                heapq.heappush(minarr, [nums1[i+1]+nums2[j],i+1,j])
                visited.add((i+1,j))
            if j+1<m:
                if (i,j+1) not in visited:
                    heapq.heappush(minarr, [nums1[i]+nums2[j+1],i, j+1])
                    visited.add((i,j+1))
            
        return ans