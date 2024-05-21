// https://leetcode.com/problems/two-sum/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indexPair;
        map<int, int> vals;
        int num = 0;

        for(int i = 0; i < nums.size(); i++){
          
            num = target - nums[i];

            if(vals.count(num)){
                indexPair.push_back(vals.at(num));
                indexPair.push_back(i);
            } else{
                vals.insert({nums[i], i});
            }
        }
        return indexPair;
    }
};
