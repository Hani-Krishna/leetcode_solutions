class Solution(object):
    def lengthOfLastWord(self, s):
        l=0
        s=s.rstrip()
        i=len(s) -1

        while i>=0 and s[i]==' ':
            i-=1

        while i>=0 and s[i]!=' ':
            l+=1
            i-=1
        return l
