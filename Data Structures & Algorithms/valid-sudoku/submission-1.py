class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for i in range(0,9):
            seen = set()
            for j in range(0,9):
                ele = board[i][j]
                if ele in seen:
                    return False
                elif ele != ".":
                    seen.add(ele)


        # cols

        for i in range(0,9):
            seen = set()
            for j in range(0,9):
                ele = board[j][i]
                if ele in seen:
                    return False
                elif ele != ".":
                    seen.add(ele)
        

        # box

        starts = [
            (0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)
        ]

        for i,j in starts:
            seen = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    ele = board[row][col]
                    if ele in seen:
                        return False
                    elif ele != ".":
                        seen.add(ele)

        return True
