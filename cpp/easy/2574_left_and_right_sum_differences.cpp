// https://leetcode.com/problems/left-and-right-sum-differences/description/
class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> res;
        int totalSum = 0;
        int leftSum = 0;
        for(auto num : nums){
            totalSum += num;
        }
        for(auto num : nums){
            res.push_back(abs(leftSum + num - (totalSum - leftSum)));
            leftSum += num;
        }
        return res;
    }
};
