class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        output = []
        pmap = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            pmap[crs].append(pre)



        visited = set()
        cycle = set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True

            cycle.add(c)
            for pre in pmap[c]:
                if dfs(pre) == False:
                    return False

            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True


        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
            
        