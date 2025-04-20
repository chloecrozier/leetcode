# https://leetcode.com/problems/count-and-say/description/?envType=daily-question&envId=2025-04-18
class Solution:
    def countAndSay(self, n: int) -> str:
        def countRuns(run):
            prev = run[0]
            count = 1
            res = ""

            for i in range(1, len(run)):
                if run[i] == prev:
                    count += 1
                else:
                    res += str(prev) + str(count)
                    prev = run[i]
                    count = 1

            res += str(prev) + str(count)
            return res

        curr = "1"
        for i in range(n - 1):
            curr = countRuns(curr)
        return curr[::-1]
