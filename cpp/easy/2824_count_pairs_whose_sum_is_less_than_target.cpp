// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/submissions/1265362287/
// Attempt #2: Time Complexity = O(nlog(n)) - Space Complexity = O(1)
class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int count = 0;
        int left = 0;
        int right = nums.size() - 1;
        while(left < right){
            if(nums[left] + nums[right] < target){
                count += right - left;
                left++;
            } else{
                right--;
            }
        }
        return count;
    }
};

// // Attempt #1: Time Complexity = O(n^2) - Space Complexity = O(1)
// class Solution {
// public:
//     int countPairs(vector<int>& nums, int target) {
//         int count = 0;
//         for(int i = 0; i < nums.size(); i++){
//             for(int j = i + 1; j < nums.size(); j++){
//                 if(nums[i] + nums[j] < target){
//                     count++;
//                 }
//             }
//         }
//         return count;
//     }
// };
