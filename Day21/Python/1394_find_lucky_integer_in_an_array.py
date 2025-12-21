class Solution(object):
    def findLucky(self, arr):
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        ans = -1
        for num in freq:
            if freq[num] == num:
                ans = max(ans, num)
        
        return ans





        
