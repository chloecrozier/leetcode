// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minVal = prices[0];
        int profit = 0;

        for(int i = 1; i < prices.size(); i++){
            minVal = min(minVal, prices[i]);
            profit = max(profit, prices[i] - minVal);
        }
        return profit;
    }
};
