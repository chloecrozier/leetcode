# https://leetcode.com/problems/closest-prime-numbers-in-range/description/?envType=daily-question&envId=2025-03-07
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        nums = [0] * (right - left)
        primes = [1] * (right + 1)
        res = [-1, -1]
        minDist = right
        i = 2
        while i * i <= right:
            if primes[i] == 1:
                for j in range(i * i, right + 1, i):
                    primes[j] = 0
            i += 1
        primes[0] = 0
        primes[1] = 0

        curr = left
        for i in range(left, right + 1):
            if primes[curr] != 1:
                curr += 1
            else:
                if curr != i and primes[i] == 1:
                    diff = i - curr
                    if minDist > diff:
                        res = [curr, i]
                        minDist = diff
                    curr = i

        return res
