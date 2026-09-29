class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L+R) // 2

            if nums[mid] == target:
                return mid

            if nums[L] <= nums[mid]:
                
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    # sending us to the right side
                    # just cause this side is sorted doesnt mean the target will be here
                    # no correlation
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1

        return -1
                