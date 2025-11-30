class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,n in enumerate(nums):
            need=target-n
            if need in seen:
                return [seen[need],i]
            seen[n]=i
