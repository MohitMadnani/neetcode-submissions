class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        long_streak = 0

        for num in nset:
            if num - 1 not in nset:
                curr_streak = 1
                curr_num = num

                while curr_num + 1 in nset:
                    curr_num += 1
                    curr_streak += 1
                
                long_streak = max(curr_streak,long_streak)

        return long_streak