// https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/?envType=daily-question&envId=2024-08-14
class Solution {
public:
    int countPairs(vector<int>& nums, int mid){
        int count = 0;
        int i = 0;
        int j = 0;
        while(j < nums.size()){
            while(abs(nums[j] - nums[i]) > mid){
                i++;
            }
            count += j - i;
            j++;
        }
        return count;
    }

    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int i = 0;
        int j = nums[nums.size() - 1] - nums[i];
        int mid = 0;
        while(i < j){
            mid = ((j - i) / 2) + i;
            if(countPairs(nums, mid) < k){
                i = mid + 1;
            } else{
                j = mid;
            }
        }
        return i;
    }
};
