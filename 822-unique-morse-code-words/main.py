class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            converted = ''
            for ch in word:
                converted += alphabet[ord(ch) - ord('a')]
            s.add(converted)
        return len(s)
        