class Solution(object):
    def subarraySum(self, nums, k):
        from collections import defaultdict

        count = 0
        prefix_sum = 0
        mp = defaultdict(int)
        mp[0] = 1  # empty prefix

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in mp:
                count += mp[prefix_sum - k]
            mp[prefix_sum] += 1

        return count
