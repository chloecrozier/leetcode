# https://leetcode.com/problems/count-items-matching-a-rule/description/
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            index = 0
        elif ruleKey == 'color':
            index = 1
        else:
            index = 2

        res = 0
        for item in items:
            if item[index] == ruleValue:
                res += 1
        return res
