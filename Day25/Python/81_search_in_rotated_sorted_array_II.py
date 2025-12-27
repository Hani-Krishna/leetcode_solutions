class Solution(object):
    def search(self, nums, target):
        for i in nums:
            if target in nums:
                return True
        return False
