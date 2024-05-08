// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        map<int, int> m;
        vector<int> v = nums;

        sort(v.begin(), v.end());

        for(int i = v.size() - 1; i >= 0; i--){
            m[v[i]] = i;
        }
        for(int i = 0; i < nums.size(); i++){
            nums[i] = m[nums[i]];
        }

        return nums;
    }
};
