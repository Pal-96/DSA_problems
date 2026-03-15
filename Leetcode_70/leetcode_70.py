class Solution:
    def climbStairs(self, n: int) -> int:
        prev_stp, stp = 1,1
        for i in range(n-1):
            temp = prev_stp
            prev_stp = stp+prev_stp
            stp = temp
        return prev_stp

        #DFS
        # stack = []
        # way=0
        # stack.append(0)
        # while stack:
        #     print(stack)
        #     cs = stack.pop()
        #     print(cs)
        #     if cs == n:
        #         way+=1
        #     if cs+1<=n:   
        #         stack.append(cs+1)
        #     if cs+2<=n:
        #         stack.append(cs+2)
        # return way

        
        #Recursion
        # way = [0]
        # dp = [0] * n
        # def meth(step):
        #     next_step = step+2
        #     if next_step==n:
        #         way[0]+=1
        #     elif next_step<n: 
        #         meth(next_step)
        #     next_step = step+1
        #     if next_step==n:
        #         way[0]+=1
        #     elif next_step<n:
        #         meth(next_step)
        #     dp[step] = way[0]
        # meth(0)
        # return way[0]