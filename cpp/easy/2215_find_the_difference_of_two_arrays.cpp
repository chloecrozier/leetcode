// https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> answers(2, vector<int>());
        set<int> s1;
        set<int> s2;

        for(int n : nums1){
            s1.insert(n);
        }
        for(int n : nums2){
            s2.insert(n);
        }
        for(int n : s1){
            if(!s2.count(n)){
                answers[0].push_back(n);
            }
        }
        for(int n : s2){
            if(!s1.count(n)){
                answers[1].push_back(n);
            }
        }
        return answers;
    }
};
