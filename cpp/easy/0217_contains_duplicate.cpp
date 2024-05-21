// https://leetcode.com/problems/contains-duplicate/description/
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> m;
        for(auto x : nums){
            if(m.count(x)){
                return true;
            }
            m[x]++;
        }
        return false;
    }
};
