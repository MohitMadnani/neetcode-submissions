class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        start = 0
        right = k

        while right <= len(nums):
            window = nums[start:right]
            ans.append(max(window))
            start +=1
            right += 1

        return ans
        
