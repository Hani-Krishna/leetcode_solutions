class Solution(object):
    def sortedSquares(self, nums):

        n = len(nums)
        result = [0] * n
        l, r = 0, n - 1
        pos = n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[pos] = nums[l] * nums[l]
                l += 1
            else:
                result[pos] = nums[r] * nums[r]
                r -= 1
            pos -= 1

        return result






        
