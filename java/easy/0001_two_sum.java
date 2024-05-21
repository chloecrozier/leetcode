// https://leetcode.com/problems/two-sum/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] locations = new int[2];
            for(int i = 0; i<nums.length-1; i++){
                for(int x = 1; x<nums.length; x++){
                    if(nums[i] + nums[x] == target && i != x){
                        locations[0] = i;
                        locations[1] = x;
                    }                    
                }

            }
        return locations;
    }
}
