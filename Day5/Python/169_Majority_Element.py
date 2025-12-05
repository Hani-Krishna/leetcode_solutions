class Solution(object):
    from collections import Counter
    def majorityElement(self, nums):
        counts = Counter(nums)
        for num, count in counts.items():
            if count > len(nums)//2:
                return num
