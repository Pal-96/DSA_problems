class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        dq = deque()
        visited = set()
        l = len(startGene)
        visited.add(startGene)
        dq.append([startGene, 0])
        comb = set(('A', 'C', 'G', 'T'))
        while dq:
            startGene, mutation = dq.popleft()
            if startGene == endGene:
                return mutation
            for i in range(0, l):
                for c in comb:
                    if startGene[i] == c:
                        continue
                    new_gene = startGene[:i] + c + startGene[i+1:]
                    if new_gene in bank and new_gene not in visited:
                        dq.append([new_gene, mutation + 1])
                        visited.add(new_gene)
        return -1