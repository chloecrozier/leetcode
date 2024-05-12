// https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged;
        int n = 0;
        int m = 0;

        // two-pointer method to merge arrays
        while(n < nums1.size() && m < nums2.size()){
            if(nums1[n] < nums2[m]){
                merged.push_back(nums1[n++]);
            } else{
                merged.push_back(nums2[m++]);
            }
        }

        while(n < nums1.size()){
            merged.push_back(nums1[n++]);
        }
        while(m < nums2.size()){
            merged.push_back(nums2[m++]);
        }
        
        if(merged.size() % 2 == 0){
            return (merged[merged.size() / 2] + merged[(merged.size() / 2) - 1]) / 2.0;
        } else{
            return merged[merged.size() / 2];
        }
    }
};
