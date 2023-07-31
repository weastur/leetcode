class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {ch:True for ch in sentence}
        return len(d.values()) == 26