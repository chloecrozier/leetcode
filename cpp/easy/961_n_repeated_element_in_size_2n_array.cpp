// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        map<int, int> m;
        for(auto n : nums){
            if(m.count(n)){
                return n;
            }
            m[n]++;
        }
        return 0;
    }
};
