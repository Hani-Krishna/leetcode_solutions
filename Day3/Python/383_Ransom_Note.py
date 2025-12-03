from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r = Counter(ransomNote)
        m = Counter(magazine)
        for ch, cnt in r.items():
            if m[ch] < cnt:
                return False
        return True
