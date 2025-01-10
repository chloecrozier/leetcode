# https://leetcode.com/problems/word-subsets/
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        subsetLetters = {}
        for subset in words2:
            for char in subset:
                if char in subsetLetters:
                    subsetLetters[char] = max(subsetLetters[char], subset.count(char))
                else:
                    subsetLetters[char] = subset.count(char)

        for word in words1:
            wordLetters = {}
            for char in word:
                if char in wordLetters:
                    wordLetters[char] += 1
                else:
                    wordLetters[char] = 1

            isSubset = True
            for key, value in subsetLetters.items():
                if not (key in wordLetters and wordLetters[key] >= value):
                    isSubset = False
            
            if isSubset:
                res.append(word) 

        return res
