// https://leetcode.com/problems/product-of-array-except-self/description/
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int count = 0;

        for(auto n : nums){
            if(!n && !count){
                count++;
            } else{
                product *= n;
            }
        }

        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 0){
                nums[i] = product;
            } else{
                if(count){
                    nums[i] = 0;
                } else{
                    nums[i] = product / nums[i];
                }
            }
        }
        return nums;
    }
};
