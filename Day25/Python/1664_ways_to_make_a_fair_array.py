class Solution(object):
    def waysToMakeFair(self, nums):

        right_even = right_odd = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even += num
            else:
                right_odd += num

        left_even = left_odd = 0
        count = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even -= num
            else:
                right_odd -= num

            # check fairness after removal
            if left_even + right_odd == left_odd + right_even:
                count += 1

            
            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num

        return count

        
