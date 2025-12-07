class Solution(object):
    def moveZeroes(self, nums):
        i = 0  
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        
        while i < len(nums):
            nums[i] = 0
            i += 1
