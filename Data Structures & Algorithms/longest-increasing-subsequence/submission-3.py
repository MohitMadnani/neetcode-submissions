class Solution:
    def lengthOfLIS(self, nums):
        LIS = [1] * len(nums) # originally all values themselves are a sequence of 1, so LIS[any number in nums] = 1

        for i in range(len(nums)-1,-1,-1): # going background bottom up
            for j in range(i+1,len(nums)): # the element ahead of i, cause that next number have to bigger than the ith number
                if nums[i] < nums[j]: # this is the check for what i just said above
                    LIS[i] = max(LIS[i],1+LIS[j]) # this is the working where we are getting the max of either itself (normally 1) or max of since LIS[j] has a sequence of its own we can attach to that so at this ith value will be the attachement of one more value (ith) where j was 1 less since it wasnt attached


        return max(LIS)