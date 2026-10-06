class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n-1):
            return False

        pmap = {i: [] for i in range(n)}

        for edge1,edge2 in edges:
            pmap[edge1].append(edge2)
            pmap[edge2].append(edge1)

        visit = set()
        def dfs(c,par):
            if c in visit:
                return False
            visit.add(c)
            for node in pmap[c]:
                if node == par:
                    continue
                if not dfs(node,c):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n





        