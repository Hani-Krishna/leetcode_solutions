class Solution(object):
    def isAnagram(self, s, t):

    # Remove spaces and convert to lowercase
        s= s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()
    
    # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
    
    # Count characters in both strings
        count1 = {}
        count2 = {}
    
        for char in s:
            count1[char] = count1.get(char, 0) + 1
        for char in t:
            count2[char] = count2.get(char, 0) + 1
    
    # Compare the dictionaries
        return count1 == count2
