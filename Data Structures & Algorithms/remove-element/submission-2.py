class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 0
                k -= 1


        nums.sort(reverse=True)
        nums[0:k] = sorted(nums[0:k])
        return k


        