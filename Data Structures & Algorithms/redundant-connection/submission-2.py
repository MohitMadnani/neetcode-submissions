class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        pmap = {i: [] for i in range(n+1)}




        def dfs(node,par):
            if visit[node]:
                return True

            visit[node] = True

            for nei in pmap[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True

            return False












        for u,v in edges:
            pmap[u].append(v)
            pmap[v].append(u)
            visit = [False] * (n+1)


            if dfs(u,-1):
                return [u,v]

        return []



            
        