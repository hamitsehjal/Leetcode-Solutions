class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [0] * len(accounts)

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # path compression
            return parent[i]
        
        def union(u,v):
            pu,pv = find(u),find(v)
            if pu == pv:
                return

            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1
        
        # email_group -> mapping email to account index
        email_group = {}

        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in email_group:
                    union(i,email_group[email]) # unionize the groups
                else:
                    email_group[email] = i
        
    
        merged = {} # mapping index to set of emails
        merged = collections.defaultdict(set)

        for i,account in enumerate(accounts):
            root = find(i)
            merged[root].update(account[1:])

        result = []
        for idx,emails in merged.items():
            name = accounts[idx][0]
            result.append([name] + list(sorted(emails)))
        
        return result
