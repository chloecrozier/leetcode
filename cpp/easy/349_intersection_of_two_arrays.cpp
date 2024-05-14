// https://leetcode.com/problems/intersection-of-two-arrays/description/
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        int max = 0;
        for(auto num : nums1){
            if(num > max){
                max = num;
            }
        }
        vector<int> seen(max + 1);
        for(auto num : nums1){
            if(!seen[num]){
                seen[num]++;
            }
        }
        for(auto num : nums2){
            if(num <= max && seen[num]){
                seen[num]--;
                res.push_back(num);
            }
        }
        return res;
    }
};
