// https://leetcode.com/problems/summary-ranges/description/
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        if(nums.size() == 0){
            return res;
        }
        int start = nums[0];
        int end = start;

        for(int i = 1; i < nums.size(); i++){
            if(end == nums[i] - 1){
                end = nums[i];
            } else{
                if(start == end){
                    res.push_back(to_string(start));
                } else{
                    res.push_back(to_string(start) + "->" + to_string(end));
                }
                start = nums[i];
                end = nums[i];
            }
        }
        if(start == end){
            res.push_back(to_string(start));
        } else{
            res.push_back(to_string(start) + "->" + to_string(end));
        }
        return res;
    }
};
