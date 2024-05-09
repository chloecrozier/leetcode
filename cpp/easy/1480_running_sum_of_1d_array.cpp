Posted Solution: https://leetcode.com/problems/running-sum-of-1d-array/solutions/5137385/simple-c-solution-w-o-extra-variables-time-complexity-o-n-space-complexity-o-n/
// https://leetcode.com/problems/running-sum-of-1d-array/description/
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++){
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};
