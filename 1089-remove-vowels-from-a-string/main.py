class Solution:
    def removeVowels(self, s: str) -> str:
        return s.translate({ord('a'):None, ord('e'): None, ord('i'): None, ord('o'): None, ord('u'): None})