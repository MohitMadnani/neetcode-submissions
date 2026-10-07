class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        pmap = {i: [] for i in range(n)}

        for u,v in edges:
            pmap[u].append(v)
            pmap[v].append(u)

        visit = set()
        
        count = 0
        def dfs(node):
            for nei in pmap[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
            

        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                count +=1
        return count
        