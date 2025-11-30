class Solution(object):
    def runningSum(self, nums):
        result =[]
        total=0
        for i in nums:
            total=total+i
            result.append(total)
        return result
