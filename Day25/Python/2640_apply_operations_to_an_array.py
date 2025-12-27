class Solution(object):
    def applyOperations(self, nums):
        result=[]
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        for i in nums:
            if i!=0:
                result.append(i)
        while len(result)<len(nums):
            result.append(0)
        return result
      
