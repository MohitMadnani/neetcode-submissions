class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L = 0
        R = len(heights) -1
        maxArea = -float("inf")
        while L < R:
            d = R-L
            h = min(heights[L], heights[R])
            maxArea = max(maxArea, d*h)
            if heights[L] < heights[R]:
                L+=1
            else:
                R -=1
        return maxArea
        