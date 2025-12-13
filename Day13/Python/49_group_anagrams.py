class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        mp = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            mp[key].append(word)

        return list(mp.values())
