from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        stack = [0]
        visited = set(stack)
        edge_changed = 0
        graph = defaultdict(list)
        directed = set()

        for a,b in connections:
            directed.add((a,b))
            graph[a].append(b)
            graph[b].append(a)
        
        while stack:
            city = stack.pop()
            for b in graph[city]:
                if b in visited:
                    continue
                if b not in visited and (city,b) in directed:
                    edge_changed+=1
                stack.append(b)
                visited.add(b)
        return edge_changed