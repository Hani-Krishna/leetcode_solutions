class Solution(object):
    def findAnagrams(self, s, p):
        from collections import Counter
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter(s[:len(p)])
        res = []

        if window == p_count:
            res.append(0)

        left = 0
        for right in range(len(p), len(s)):
            window[s[right]] += 1
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]

            left += 1

            if window == p_count:
                res.append(left)

        return res
