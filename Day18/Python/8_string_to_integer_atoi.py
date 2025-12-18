class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        # 1) skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # if string is empty after spaces
        if i == n:
            return 0
        
        # 2) handle sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # 3) read digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign
        
        # 4) clamp to 32-bit range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num

        
