from string import ascii_lowercase

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for letter in ascii_lowercase:
            first = s.find(letter)
            if first == -1:
                continue
            second = s.find(letter, first + 1)
            if distance[ord(letter) - ord('a')] != second - first - 1:
                return False
        return True