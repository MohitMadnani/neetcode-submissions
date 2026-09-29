class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""


        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        left = 0
        right = 0

        best = (float("inf"),None,None)
        while right < len(s):
            c = s[right]

            window[c] = window.get(c,0) + 1

            if c in need and window[c] == need[c]:
                formed +=1

            while formed == required and left <= right:
                if right - left + 1 < best[0]:
                    best = (right - left +1,left, right)


                d = s[left]

                window[d] = window.get(d) - 1
                if d in need and window[d] < need[d]:
                    formed -=1

                left +=1

            right +=1

        if best[0] == float("inf"):
            return ""

        L, R = best[1], best[2]
        return s[L:R+1]

