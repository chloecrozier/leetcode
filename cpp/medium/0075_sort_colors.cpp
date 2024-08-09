// https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2024-08-10
class Solution {
public:
    void sortColors(vector<int>& nums) {
        // No Extra Space | Two Pointers
        int i = 0;
        int j = nums.size() - 1;
        int k = 0;
        for(int k = 0; k <= j; k++){
            if(nums[k] == 0){
                swap(nums[i], nums[k]);
                i++;
            }
            if(nums[k] == 2){
                swap(nums[j], nums[k]);
                k--;
                j--;
            }
        }

        // // Extra Space Solution
        // int count[3];
        // for(int num : nums){
        //     count[num]++;
        // }
        // int j = 0;
        // for(int i = 0; i < nums.size(); i++){
        //     if(count[j] == 0){
        //         j++;
        //         i--;
        //     } else{
        //         nums[i] = j;
        //         count[j]--;
        //     }
        // }
    }
};
