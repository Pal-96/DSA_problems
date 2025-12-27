class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        stack = []
        n = len(isConnected)
        visited = ['F']*n
        province = 0
        for i in range(0, n):
            if visited[i] == 'F':
                stack.append(i)
                visited[i] = 'T'
                province+=1
            while stack:
                row = stack.pop()
                for col in range (0, n):
                    if row !=col:
                        if isConnected[row][col] == 1 and visited[col]!='T':
                            stack.append(col)
                            visited[col] = 'T'
        return province
        