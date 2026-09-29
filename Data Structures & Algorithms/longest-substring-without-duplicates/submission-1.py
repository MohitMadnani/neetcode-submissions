class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    curr_length = len(s[i:j+1])
                    if max_length < curr_length:
                        max_length = curr_length

                else:
                    break
        return max_length

        