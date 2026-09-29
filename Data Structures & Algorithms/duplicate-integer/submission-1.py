class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set()

        for i in range(len(nums)):
            if nums[i] not in n:
                n.add(nums[i])
            else:
                return True

        return False