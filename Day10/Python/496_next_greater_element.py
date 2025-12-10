class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        next_greater = {}

        for num in nums2:
        # Resolve next greater for previous smaller numbers
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

    # Anything left in stack has no next greater
        for num in stack:
            next_greater[num] = -1

    # Build answer for nums1
        return [next_greater[n] for n in nums1]
