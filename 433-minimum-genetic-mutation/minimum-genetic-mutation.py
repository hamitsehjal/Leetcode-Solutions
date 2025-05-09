class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = collections.deque([(startGene, 0)])
        geneSet = ["A", "C", "G", "T"]

        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations

            for i in range(8):
                genome = gene[i]
                for g in geneSet:
                    if g == genome:
                        continue
                    nextMutation = gene[:i] + g + gene[i + 1 :]
                    if nextMutation in bank:
                        bank.remove(nextMutation)
                        queue.append((nextMutation, mutations + 1))

        return -1
