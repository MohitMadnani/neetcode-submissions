class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        pmap = {i: [] for i in range(n)}

        for u,v in edges:
            pmap[u].append(v)
            pmap[v].append(u)

        visit = [False] * n
        
        count = 0
        def dfs(node):
            for nei in pmap[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
            
                







        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                count +=1
        return count
        