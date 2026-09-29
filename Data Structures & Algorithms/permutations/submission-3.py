class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []

        def build(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return



            for num in nums:
                if num in cur:
                    continue
                cur.append(num)
                build(cur)
                cur.pop()

        build([])
        return res
        