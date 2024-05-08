# https://leetcode.com/problems/richest-customer-wealth/description/
class Solution(object):
    def maximumWealth(self, accounts):
            ans = [0] * len(accounts)
            
            for i in range(len(accounts)):
                ans[i] = sum(accounts[i])
                
            return max(ans)
