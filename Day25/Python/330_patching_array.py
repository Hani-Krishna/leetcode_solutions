class Solution(object):
    def minPatches(self, nums, n):
        number=1
        adding=0
        i=0
        while number<=n:
            if i < len(nums) and nums[i] <=number:
                number += nums[i]
                i += 1
            else:
                number+= number
                adding+= 1
        return adding



        
