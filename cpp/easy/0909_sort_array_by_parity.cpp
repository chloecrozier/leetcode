// https://leetcode.com/problems/sort-array-by-parity/
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        partition(nums.begin(), nums.end(), [](int num){return num % 2 == 0;});
        return nums;

        // int even = 0;
        // int odd = nums.size() - 1;
        // int i = 0;
        // while(i < nums.size() && even < odd){
        //     if(nums[i] % 2 == 0){
        //         swap(nums[i], nums[even]);
        //         even++;
        //         i++;
        //     } else{
        //         swap(nums[i], nums[odd]);
        //         odd--;
        //     }
        // }
        // return nums;
    }
};
