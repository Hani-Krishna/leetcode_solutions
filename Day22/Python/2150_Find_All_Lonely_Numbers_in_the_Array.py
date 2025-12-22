class Solution(object):
    def findLonely(self, nums):
        freq = {}

        # count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = []

        # check lonely condition
        for num in freq:
            if freq[num] == 1 and (num - 1) not in freq and (num + 1) not in freq:
                result.append(num)

        return result





            


        
