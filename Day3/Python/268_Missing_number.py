class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        exp=n*(n+1)//2
        actual=sum(nums)
        return exp-actual
