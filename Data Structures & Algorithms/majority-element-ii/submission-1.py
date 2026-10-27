class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lnums = Counter(nums)
        res = []

        for key in lnums:
            if lnums[key] > len(nums)//3:
                res.append(key)


        return res

        