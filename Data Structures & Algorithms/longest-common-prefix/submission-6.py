class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            count = 0
            while j < len(strs[i]) and j < len(prefix):
                if prefix[j] == strs[i][j]:
                    count += 1
                else:
                    break
                j+=1
            prefix = strs[0][0:count]

        return prefix


        