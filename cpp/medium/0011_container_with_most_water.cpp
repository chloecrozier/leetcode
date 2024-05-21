// https://leetcode.com/problems/container-with-most-water/description/
class Solution {
public:
    int maxArea(vector<int>& h) {
        int l = 0, r = h.size() - 1;
        int maxVol = 0;
        while(l < r){
            if(h[l] > h[r]){
                maxVol = max(maxVol, (r - l) * h[r--]);
            }else{
                maxVol = max(maxVol, (r - l) * h[l++]);
            }
        }
        return maxVol;
    }
};
