class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}":"{","]":"[",")":"("}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)

            elif c in ")}]":
                if not stack:
                    return False
                if stack.pop() != d[c]:
                    return False


        return len(stack) == 0