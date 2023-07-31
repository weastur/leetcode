class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            idx = 0
        elif ruleKey == 'color':
            idx = 1
        else:
            idx = 2
        ans = 0
        for item in items:
            ans += item[idx] == ruleValue
        return ans