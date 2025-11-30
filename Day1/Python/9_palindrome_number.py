class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        rev = 0
        original = x
        
        while x > 0:
            rev = (rev * 10) + (x % 10)   # use x, not X
            x = x // 10
        
        return rev == original
