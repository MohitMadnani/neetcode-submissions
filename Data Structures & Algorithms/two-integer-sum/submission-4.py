class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for j in range(len(nums)):
            y = target - nums[j]

            if y in h and h[y] != j:
                return [j, h[y]]
        