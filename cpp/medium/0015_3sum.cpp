// https://leetcode.com/problems/3sum/description/
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> triplets;
        int l, r;
        for(int iter = 0; iter < nums.size(); iter++){
            if(iter > 0 && nums[iter] == nums[iter - 1]){
                // cout << "dupe" << endl;
            } else{
                l = iter + 1;
                r = nums.size() - 1;
                while(l < r){
                    if(nums[iter] + nums[l] + nums[r] == 0){
                        triplets.push_back({nums[iter], nums[l], nums[r]});
                        l++;
                        while(l < r && nums[l] == nums[l - 1]){
                            l++;
                        }
                    } else if(nums[iter] + nums[l] + nums[r] > 0){
                        r--;
                    } else{
                        l++;
                    }
                }
            }
        }
        return triplets;
    }
};
