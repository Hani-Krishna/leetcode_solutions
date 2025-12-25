class Solution(object):
    def frequencySort(self, nums):
        from collections import Counter
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))

        
