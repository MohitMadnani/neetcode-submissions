class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []

        l = 0
        r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l][0] == nums2[r][0]:
                ans.append([nums1[l][0],nums1[l][1]+nums2[r][1]])
                l+=1
                r+=1

            elif nums1[l][0] < nums2[r][0]:
                ans.append(nums1[l])
                l+=1
            else:
                ans.append(nums2[r])
                r+=1


        ans.extend(nums1[l:])
        ans.extend(nums2[r:])

        return ans
                

        
