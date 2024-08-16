// https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int min1 = INT_MAX;
        int max1 = INT_MIN;
        int minI, maxI;
        for(int i = 0; i < arrays.size(); i++){
            if(min1 > arrays[i][0]){
                min1 = arrays[i][0];
                minI = i;
            }
            if(max1 < arrays[i][arrays[i].size() - 1]){
                max1 = arrays[i][arrays[i].size() - 1];
                maxI = i;
            }
        }
        // if the max/min were found at the same index, we will find whether the 2nd max/min maximizes the dist
        if(minI == maxI){
            int min2 = INT_MAX;
            int max2 = INT_MIN;
            for(int i = 0; i < arrays.size(); i++){
                if(min2 > arrays[i][0] && i != minI){
                    min2 = arrays[i][0];
                }
                if(max2 < arrays[i][arrays[i].size() - 1] && i != maxI){
                    max2 = arrays[i][arrays[i].size() - 1];
                }
            }
            return max((abs(max2 - min1)), (abs(max1 - min2)));
        } else{
            return abs(max1 - min1);
        }
    }
};
