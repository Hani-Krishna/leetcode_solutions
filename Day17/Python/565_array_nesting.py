class Solution(object):
    def arrayNesting(self, nums):
        max_len = 0

        for i in range(len(nums)):
            count = 0
            while nums[i] != -1:
                nxt = nums[i]
                nums[i] = -1
                i = nxt
                count += 1
            max_len = max(max_len, count)

        return max_len
