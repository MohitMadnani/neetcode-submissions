class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        pmap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pmap[crs].append(pre)


        visited = set()
        def dfs(c):
            if c in visited:
                return False
            if pmap[c] == []:   # Memoization
                return True

            visited.add(c)
            for pre in pmap[c]:
                if not dfs(pre):
                    return False

            visited.remove(c)
            pmap[c] = []
            return True




        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        










