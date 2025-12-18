class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        dq = deque()
        dq.append([startGene, 0])
        visited = set()
        visited.add(startGene)
        choices = set(('A', 'C', 'G', 'T'))
        while dq:
            gen e, steps = dq.popleft()
            if gene == endGene:
                return steps
            
            for i, s in enumerate(gene):
                for c in choices:
                    if s != c:
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in bank and new_gene not in visited:
                            visited.add(new_gene)
                            dq.append([new_gene, steps+1])
        return -1