// https://leetcode.com/problems/majority-element/description/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0;
        int count = 0;
        for(auto num : nums){
            if(count == 0){
                candidate = num;
                count++;
            } else{
                if(candidate == num){
                    count++;
                } else{
                    count--;
                }
            }
            if(count > nums.size() / 2){
                return candidate;
            }
        }
        return candidate;
    }
};
