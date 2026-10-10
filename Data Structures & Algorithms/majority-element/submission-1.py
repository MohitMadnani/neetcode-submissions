class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        res = maxcount = 0



        for num in nums:
            hmap[num] +=1
            if maxcount < hmap[num]:
                res = num 
                maxcount = hmap[num]
        return res





        