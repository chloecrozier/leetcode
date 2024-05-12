// https://leetcode.com/problems/median-of-two-sorted-arrays/description/

// Answer #1:
// 	Time Complexity:  O(n + m)
//      Space Complexity: O(n) (additional vector used to store merged results)
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

// Answer #2:
//	Time Complexity: O(n + m)
//	Space Complexity: O(1)
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        bool odd = (nums1.size() + nums2.size()) % 2;
        int i = 0;
        int j = (nums1.size() + nums2.size()) / 2;
        int n = 0;
        int m = 0;
        int med = 0;
        int medNext = 0;
        
        if(nums1.size() == 0){
            if(odd){
                return nums2[nums2.size() / 2];
            } else{
                return (nums2[nums2.size() / 2] + nums2[(nums2.size() / 2) - 1]) / 2.0; 
            }
        }
        if(nums2.size() == 0){
            if(odd){
                return nums1[nums1.size() / 2];
            } else{
                return (nums1[nums1.size() / 2] + nums1[(nums1.size() / 2) - 1]) / 2.0; 
            }
        }

	// two pointer method using expected median index or indices
        while(n < nums1.size() && m < nums2.size()){
            i++;
            if(nums1[n] < nums2[m]){
                med = nums1[n++];
            } else{
                med = nums2[m++];
            }

            if((i == j && !odd) || (i - 1 == j && odd)){
                if(odd){
                    return med;
                } else{
                    if(n < nums1.size() && m < nums2.size()){
                        medNext = (min(nums1[n], nums2[m]));
                    } else if(n < nums1.size()){
                        medNext = nums1[n];
                    } else{
                        medNext = nums2[m];
                    }
                    return (med + medNext) / 2.0; 
                }
            }
        }

        if(n < nums1.size()){
            if(odd){
                if(i != j){
                    return nums1[n + j - i];
                } else{
                    return nums1[n];
                }
            } else{
                if(i != j){
                    return (nums1[n + j - i] + nums1[n + j - i - 1]) / 2.0;
                } else{
                    return (med + nums1[n]) / 2.0; 
                }
            }
        }
        if(m < nums2.size()){
            if(odd){
                if(i != j){
                    return nums2[m + j - i];
                } else{
                    return nums2[m];
                }
            } else{
                if(i != j){
                    return (nums2[m + j - i] + nums2[m + j - i - 1]) / 2.0;
                } else{
                    return (med + nums2[m]) / 2.0; 
                }
            }
        }
        return 0;
    }
};
