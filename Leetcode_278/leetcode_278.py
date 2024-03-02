# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # vl = list(range(1,n+1))
        # size = len(vl)
        if n==1:
            return n
        else:
            si = 1
            li = n
            while(si<=li):
                mid = (si+li)>>1
                if isBadVersion(mid) and not(isBadVersion(mid-1)):
                    return mid
                elif isBadVersion(mid-1):
                    li = mid-1
                elif isBadVersion(mid+1):
                    si = mid+1
                else:
                    si = mid+1
