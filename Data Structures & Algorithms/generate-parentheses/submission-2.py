class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(currString,opening,closing):
            if opening > n or closing > n:
                return
            if opening == n and closing == n:
                res.append(currString)
                return


            
            if opening < n:
                backtracking(currString + "(", opening + 1,closing)

            if closing < opening:
                backtracking(currString + ")", opening,closing + 1)






        backtracking("",0,0)
        return res
        