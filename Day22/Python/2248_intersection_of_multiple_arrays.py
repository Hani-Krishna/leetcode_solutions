class Solution(object):
    def intersection(self, nums):
        freq = {}
        total_arrays = len(nums)

        for arr in nums:
            for num in arr:
                freq[num] = freq.get(num, 0) + 1

        result = []
        for num in freq:
            if freq[num] == total_arrays:
                result.append(num)

        return sorted(result)

        
