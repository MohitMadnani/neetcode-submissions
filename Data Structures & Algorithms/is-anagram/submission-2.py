class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        h1 = Counter(s)
        h2 = Counter(t)

        if h1 != h2:
            return False
        return True
