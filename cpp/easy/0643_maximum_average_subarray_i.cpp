// https://leetcode.com/problems/maximum-average-subarray-i/
class Solution {
public:
    double findMaxAverage(vector<int>& n, int k) {
        double maxAve = INT_MIN, sum = 0;
        for(int i = 0; i < n.size(); i++){
            sum += n[i];
            if(i >= k - 1){
                maxAve = max(maxAve, sum / k);
                sum -= n[i - k + 1];
            }
        }
        return maxAve;
    }
};
