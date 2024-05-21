// https://leetcode.com/problems/increasing-triplet-subsequence/description/
class Solution {
public:
    bool increasingTriplet(vector<int>& n) {
        if(n.size() < 3){
            return false;
        }
        int i = INT_MAX, j = INT_MAX;
        for(int k : n){
            if(k <= i){
                i = k;
            } else if(k <= j){
                j = k;
            } else{
                return true;
            }
        }
        return false;
    }
};
