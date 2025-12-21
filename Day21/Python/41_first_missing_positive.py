class Solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)

        # Step 1: Ignore numbers <=0 or >n
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark presence using index sign
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                nums[val - 1] = -abs(nums[val - 1])

        # Step 3: Find first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

        



    




        
