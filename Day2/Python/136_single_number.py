class Solution(object):
    def singleNumber(self, nums):
        nonre=0
        for n in nums:
            nonre ^= n
        return nonre
