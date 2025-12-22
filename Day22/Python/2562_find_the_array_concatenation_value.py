class Solution(object):
    def findTheArrayConcVal(self, nums):
        summ=0
        i = 0
        j = len(nums) - 1 
        while i <= j:
            if i == j:
                summ += nums[i]
            else:
                summ += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1 
        return summ
