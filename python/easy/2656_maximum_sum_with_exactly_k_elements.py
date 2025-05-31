# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (max(nums) * k) + (((k - 1) * k) // 2)
