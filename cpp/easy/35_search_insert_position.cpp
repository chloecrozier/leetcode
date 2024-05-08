// https://leetcode.com/problems/search-insert-position/description/
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == target){
                return i;
            } else if(i < nums.size() - 1){
                if((nums[i] < target) && (nums[i+1] > target)){
                    return i + 1;
                }
            }
            if(nums[0] > target){
                return 0;
            }
        }
        return nums.size();
    }
};
