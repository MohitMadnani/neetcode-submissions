class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[len(s)] = True


        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)<=len(s) and s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]
                # basically once we found the above line (line 11) meaning we've found a way to break it and that broken part is there so we can sto the for w in dict in loop here
                if dp[i]:
                    break


        return dp[0]
        