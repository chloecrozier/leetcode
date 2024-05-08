// https://leetcode.com/problems/squares-of-a-sorted-array/description/
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int start = 0;
        int end = nums.size() - 1;
        int maxIndex = end;
        vector<int> v(maxIndex + 1, 0);

        while(maxIndex >= 0){
            if(abs(nums[start]) > abs(nums[end])){
                v[maxIndex--] = nums[start] * nums[start++];
            } else{
                v[maxIndex--] = nums[end] * nums[end--];
            }
        }
        return v;

        // for(auto &x : nums){
        //     x *= x;
        // }
        // sort(nums.begin(), nums.end());
        // return nums;
    }
};
