# https://leetcode.com/problems/relative-ranks/description/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        for i in range(len(score)):
            score[i] = (score[i], i)

        places = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        place = 0
        res = []

        score.sort(reverse=True)
        for i in range(len(score)):
            if place < 3:
                res.append((places[place], score[i][1]))
            else:
                res.append((str(place + 1), score[i][1]))
            place += 1

        res = sorted(res, key=lambda x: x[1])
        return [x[0] for x in res]
