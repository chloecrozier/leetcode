# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-09
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        length = len(pref)
        for word in words:
            if word[0:length] == pref:
                count += 1
        return count
