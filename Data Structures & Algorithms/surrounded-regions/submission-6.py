class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])


        safe = [[False] * cols for _ in range(rows)]

        

        def dfs(r,c):



            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr,nc = r+dr, c+dc
                if (0 <= nr < rows and 0 <= nc < cols) and board[nr][nc] == "O" and not safe[nr][nc]:
                    safe[nr][nc] = True
                    dfs(nr,nc)
                




        




        
        for c in range(cols):
            if board[0][c] == "O":
                safe[0][c] = True

            if board[rows-1][c] == "O":
                safe[rows-1][c] = True


        for r in range(rows):
            if board[r][0] == "O":
                safe[r][0] = True


            if board[r][cols-1] == "O":
                safe[r][cols-1] = True



        for row in range(rows):
            for col in range(cols):
                if safe[row][col] == True:
                    dfs(row,col)


        for rw in range(rows):
            for cw in range(cols):
                if board[rw][cw] == "O" and safe[rw][cw] != True:
                    board[rw][cw] = "X"


            
        

            
                
















    


        
        