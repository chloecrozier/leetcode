# https://leetcode.com/problems/longest-happy-string/description/?envType=daily-question&envId=2024-10-16
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        consecutiveA = 0
        consecutiveB = 0
        consecutiveC = 0
        
        while a or b or c:
            if a >= b and a >= c:
                if a >= 2 and consecutiveA < 1:
                    res += 'aa'
                    a -= 2
                    consecutiveA = 2
                    consecutiveB = 0
                    consecutiveC = 0
                elif a == 1 and consecutiveA < 2:
                    res += 'a'
                    a -= 1
                    consecutiveA = 1
                    consecutiveB = 0
                    consecutiveC = 0
                else:
                    if b > 0 and consecutiveB < 2:
                        res += 'b'
                        b -= 1
                        consecutiveB += 1
                        consecutiveA = 0
                        consecutiveC = 0
                    elif c > 0 and consecutiveC < 2:
                        res += 'c'
                        c -= 1
                        consecutiveC += 1
                        consecutiveA = 0
                        consecutiveB = 0
                    else:
                        return res

            elif b >= a and b >= c:
                if b >= 2 and consecutiveB < 1:
                    res += 'bb'
                    b -= 2
                    consecutiveB = 2
                    consecutiveA = 0
                    consecutiveC = 0
                elif b == 1 and consecutiveB < 2:
                    res += 'b'
                    b -= 1
                    consecutiveB = 1
                    consecutiveA = 0
                    consecutiveC = 0
                else:
                    if a > 0 and consecutiveA < 2:
                        res += 'a'
                        a -= 1
                        consecutiveA += 1
                        consecutiveB = 0
                        consecutiveC = 0
                    elif c > 0 and consecutiveC < 2:
                        res += 'c'
                        c -= 1
                        consecutiveC += 1
                        consecutiveA = 0
                        consecutiveB = 0
                    else:
                        return res

            else: 
                if c >= 2 and consecutiveC < 1:
                    res += 'cc'
                    c -= 2
                    consecutiveC = 2
                    consecutiveA = 0
                    consecutiveB = 0
                elif c == 1 and consecutiveC < 2:
                    res += 'c'
                    c -= 1
                    consecutiveC = 1
                    consecutiveA = 0
                    consecutiveB = 0
                else:
                    if a > 0 and consecutiveA < 2:
                        res += 'a'
                        a -= 1
                        consecutiveA += 1
                        consecutiveB = 0
                        consecutiveC = 0
                    elif b > 0 and consecutiveB < 2:
                        res += 'b'
                        b -= 1
                        consecutiveB += 1
                        consecutiveA = 0
                        consecutiveC = 0
                    else:
                        return res
        return res
