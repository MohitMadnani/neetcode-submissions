class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = []

        for c in s2:
            window.append(c)
            if len(window) > len(s1):
                window.pop(0)
            if len(window) == len(s1):
                s1counter = Counter(s1)
                windowcounter = Counter(window)

                if s1counter == windowcounter:
                    return True


        return False


