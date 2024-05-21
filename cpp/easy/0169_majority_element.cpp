// https://leetcode.com/problems/majority-element/description/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for(int i = 0; i <= nums.size() / 2; i++){
            if(nums[i] == nums[i + (nums.size() / 2)]){
                return nums[i];
            }
        }
        return -1;

        // map<int, int> count;
        // for(auto x : nums){
        //     count[x]++;
        //     if(count[x] > nums.size() / 2){
        //         return x;
        //     }
        // }
        // return -1;
    }
};
