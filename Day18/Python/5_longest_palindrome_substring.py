class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length only for comparison

        for i in range(len(s)):
            len1 = expand(i, i)       # odd palindrome
            len2 = expand(i, i + 1)   # even palindrome
            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]   # SUBSTRING is returned

        
