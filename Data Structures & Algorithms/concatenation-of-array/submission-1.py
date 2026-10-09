class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        twon = 2 * n
        ans = [0] * twon

        count = 0
        for i in range(n):
            ans[i] = nums[i]
            count +=1


        for j in range(count,twon):
            ans[j] = nums[j-count]


        return ans

        
        