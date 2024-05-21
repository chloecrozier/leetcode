// https://leetcode.com/problems/merge-sorted-array/description/
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int curr = 0;
        int j = 0;
        for(int i = 0; i < m + j; i++){
            if(j < n && nums1[i] > nums2[j]){
                nums1.insert(nums1.begin() + i, nums2[j]);
                nums1.pop_back();
                j++;
            }
        }
        for(int i = n - 1; i >= j; i--){
            nums1.insert(nums1.begin() + m + j, nums2[i]);
            nums1.pop_back();
        }
    }
};
