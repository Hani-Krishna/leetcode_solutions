class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []

        for i, w in enumerate(words, start=1):
            if w[0] in vowels:
                goat = w + "ma"
            else:
                goat = w[1:] + w[0] + "ma"
            
            goat += "a" * i
            result.append(goat)

        return " ".join(result)
