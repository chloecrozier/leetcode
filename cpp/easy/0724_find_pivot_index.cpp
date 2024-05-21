// https://leetcode.com/problems/find-pivot-index/
class Solution {
public:
    int pivotIndex(vector<int>& n) {
        int leftSum = 0, rightSum = 0, pivot = 0;
        for(int i = 0; i < n.size(); i++){
            rightSum += n[i];
        }
        for(int i = 0; i < n.size(); i++){
            leftSum += pivot;
            rightSum -= n[i];
            pivot = n[i];
            if(leftSum == rightSum){
                return i;
            }
        }
        return -1;
    }
};
