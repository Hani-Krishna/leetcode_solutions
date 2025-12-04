class Solution(object):
    def isPalindrome(self, s):
        str1="".join([ch for ch in s if ch.isalnum()])
        str1=str1.lower()
        return str1==str1[::-1]
