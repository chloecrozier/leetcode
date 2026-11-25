// https://leetcode.com/problems/two-sum/submissions/2203017636/
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, usize> = HashMap::new();
        for i in 0..nums.len(){
            if seen.contains_key(&(target - nums[i])){
                return vec![seen[&(target - nums[i])] as i32, i as i32];

            } else{
                seen.insert(nums[i], i);
            }
        }
        return vec![];
    }
}
