import heapq
class MedianFinder:
    def __init__(self):
        self.maxsmallheap = []
        self.minlargeheap = []
    def addNum(self, num: int):
        # print("Num:", num)
        if len(self.maxsmallheap)==0:
            heapq.heappush(self.maxsmallheap, -num)
        elif num>=-self.maxsmallheap[0] and len(self.minlargeheap)<=len(self.maxsmallheap):
            heapq.heappush(self.minlargeheap, num)
        elif num<-self.maxsmallheap[0]:
            if len(self.maxsmallheap)<len(self.minlargeheap)+1:
                heapq.heappush(self.maxsmallheap, -num)
            else:
                heapq.heappush(self.minlargeheap,-heapq.heappop(self.maxsmallheap))
                heapq.heappush(self.maxsmallheap, -num)
        elif num>=self.minlargeheap[0] and len(self.minlargeheap)>=len(self.maxsmallheap):
            heapq.heappush(self.maxsmallheap,-heapq.heappop(self.minlargeheap))
            heapq.heappush(self.minlargeheap, num)
        elif num>=-self.maxsmallheap[0] and len(self.maxsmallheap)<len(self.minlargeheap):
            heapq.heappush(self.maxsmallheap, -num)
        # print(self.maxsmallheap)
        # print(self.minlargeheap)
    
    def findMedian(self):
        n = len(self.minlargeheap)
        m = len(self.maxsmallheap)
        if n==m:
            return (self.minlargeheap[0]+(-self.maxsmallheap[0]))/2
        if n>m:
            return self.minlargeheap[0]
        if m>n:
            return -self.maxsmallheap[0]
        
