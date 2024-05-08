// https://leetcode.com/problems/remove-element/description/
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int counter = nums.size();
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == val){
                nums.erase(nums.begin() + i);
                counter--;
                i--;
            }
        }
        return counter;
    }
};
