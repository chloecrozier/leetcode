// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int left = 0;
        int right = numbers.size() - 1;
        int sum = 1001;
        while(left != right && sum != target){
            sum = numbers[left] + numbers[right];
            if(sum == target){
                res.push_back(left + 1);
                res.push_back(right + 1);
            } else if(sum < target){
                left++;
            } else{
                right--;
            }
        }
        return res;
    }
};
