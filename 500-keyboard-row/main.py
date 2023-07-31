class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = set('qwertyuiop')
        s = set('asdfghjkl')
        t = set('zxcvbnm')
        ret = []
        for word in words:
            current = set(word.lower())
            if current.issubset(f) or current.issubset(s) or current.issubset(t):
                ret.append(word)
        return ret