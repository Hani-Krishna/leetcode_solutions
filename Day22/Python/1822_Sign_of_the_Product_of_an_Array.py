class Solution(object):
    def arraySign(self, nums):
        negative_count = 0

        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                negative_count += 1

        return -1 if negative_count % 2 == 1 else 1

        
