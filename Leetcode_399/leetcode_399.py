class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
            # a-> [b, a/b], b-> [[a, b/a], [c, b/c]], c-> [b, c/b]

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            deq = deque() #[[a,1], [b, a/b]]
            visited = set() #[a, b]
            deq.append([src, 1]) 
            visited.add(src)
            while deq:
                n,w = deq.popleft() #b, a/b
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visited:
                        deq.append([nei, w * weight])
                        visited.add(nei)
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]
        





        