// https://leetcode.com/problems/shuffle-the-array/description/
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        // TC: O(n) - SC: O(n) (in-place)
        for(int i = 0; i < n; i++){
            nums[i] += 10000 * nums[i + n];
        }
        for(int i = n - 1; i >= 0; i--){
            nums[2 * i + 1] = nums[i] / 10000;
            nums[2 * i] = nums[i] % 10000;
        }
        return nums;

        // // TC: O(n) - SC: O(2n)
        // vector<int> res;
        // for(int i = 0; i < n; i++){
        //     res.push_back(nums[i]);
        //     res.push_back(nums[i+n]);
        // }
        // return res;
    }
};
