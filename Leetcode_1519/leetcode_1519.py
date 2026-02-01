class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        ans = [0] * n
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        
        def dfs(root):
            cnt = Counter()
            if root not in visited:
                visited.add(root)
                cnt[labels[root]] += 1
                for child in graph[root]:
                    if child not in visited:
                        cnt = cnt + dfs(child)
                ans[root] = cnt[labels[root]]
            return cnt
        dfs(0)
        return ans