// https://leetcode.com/problems/find-the-highest-altitude/description/
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int max = 0, alt = 0;
        for(auto x : gain){
            alt += x;
            if(alt > max){
                max = alt;
            }
        }
        return max;
    }
};
