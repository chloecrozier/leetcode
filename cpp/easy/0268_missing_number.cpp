// https://leetcode.com/problems/missing-number/description/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int expectedSum = 0;
        int actualSum = 0;

        for(int i = 0; i < nums.size(); i++){
            expectedSum += i;
            actualSum += nums[i];
        }
        return expectedSum + nums.size() - actualSum;
    }
};
