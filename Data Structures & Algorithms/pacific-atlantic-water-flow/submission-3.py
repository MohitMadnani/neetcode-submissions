class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(node,visited):
            r,c = node

            if node in visited:
                return
            
            visited.add(node)
            if r - 1 >= 0 and heights[r-1][c] >= heights[r][c]:
                dfs((r-1,c),visited)

            if r + 1 < rows and heights[r+1][c] >= heights[r][c]:
                dfs((r+1,c),visited)

            if c - 1 >= 0 and heights[r][c-1] >= heights[r][c]:
                dfs((r,c-1),visited)

            if c+1 < cols and heights[r][c+1] >= heights[r][c]:
                dfs((r,c+1),visited)

            return visited
        
        
        rows = len(heights)
        cols = len(heights[0])


        atl = set()
        pac = set()


        for c in range(cols):
            pac.add((0,c)) # top
            atl.add((rows-1,c)) # bottom

        for r in range(rows):
            pac.add((r,0)) # left
            atl.add((r,cols-1)) # right



        visited_pac = set()
        visited_atl = set()


        for node in pac:
            dfs(node,visited_pac)

        for node in atl:
            dfs(node,visited_atl)


        output = []

        for node in visited_pac:
            if node in visited_atl:
                output.append(node)

        return output

        
        

