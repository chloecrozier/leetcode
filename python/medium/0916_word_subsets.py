# https://leetcode.com/problems/word-subsets/
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = {}
        res = []

        word2 = {}
        for subset in words2:
            for char in subset:
                if char in word2:
                    word2[char] += 1
                else:
                    word2[char] = 1
        for key, value in word2.items():
            print(key, value)

        for word in words1:
            count = 0
            word1 = {}
            for char in word:
                if char in word1:
                    word1[char] += 1
                else:
                    word1[char] = 1

                isSubset = True
                for key, value in word2.items():
                    if not (key in word1 and word1[key] >= value):
                        isSubset = False
                
                if isSubset:
                    count += 1
                    
            
            if count == len(words2):
                res.append(word)                
            count = 0

        return res
