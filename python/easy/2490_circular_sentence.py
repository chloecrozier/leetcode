# https://leetcode.com/problems/circular-sentence/description/?envType=daily-question&envId=2025-01-14
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i in range(0, len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        
        return words[0][0] == words[-1][-1]
