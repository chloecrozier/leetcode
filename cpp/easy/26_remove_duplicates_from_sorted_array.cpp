// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0;
        int curr = nums[0];

        for(int i = 1; i < nums.size(); i++){
            if(curr == nums[i]){
                nums.erase(nums.begin() + i);
                count++;
                i--;
            }
            curr = nums[i];
        }
        return nums.size();
    }
};
