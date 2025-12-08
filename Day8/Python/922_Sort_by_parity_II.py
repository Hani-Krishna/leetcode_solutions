class Solution(object):
    def sortArrayByParityII(self, nums):
        n = len(nums)
        res = [0] * n
        even = 0
        odd = 1

        for x in nums:
            if x % 2 == 0:
                res[even] = x
                even += 2
            else:
                res[odd] = x
                odd += 2

        return res
