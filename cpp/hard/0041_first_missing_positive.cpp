// https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-08-10
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int last = nums.size() - 1;
        for(int i = 0; i <= last; i++){
            if(nums[i] <= 0 || nums[i] > nums.size()){
                nums[i] = 0;
                swap(nums[i--], nums[last--]);
            } else{
                if(nums[i] != i + 1){
                    if(nums[i] == nums[nums[i] - 1]){
                        nums[i] = 0;
                    } else{
                        swap(nums[i], nums[nums[i] - 1]);
                        i--;
                    }
                }
            }
        }
        int min = 1;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != 0){
                if(nums[i] == min){
                    min++;
                }
            }
        }
        return min;
    }
};
