class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        h1 = {}
        for char in s:
            h1[char] = h1.get(char,0) + 1
        h2 = {}
        for char in t:
            h2[char] = h2.get(char,0)+1
        

        if h1 != h2:
            return False
        return True
