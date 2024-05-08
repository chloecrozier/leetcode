# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
class Solution(object):
    def mostWordsFound(self, sentences):
        max = sentences[0].count(" ") + 1
        for i in range (1, len(sentences)):
            if max < (sentences[i].count(" ") + 1):
                max = sentences[i].count(" ") + 1
        return max
