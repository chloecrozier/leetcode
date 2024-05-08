// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int k) {
        int max = candies[0];
        vector<bool> res;
        for(auto num : candies){
            if(num > max){
                max = num;
            }
        }

        for(auto num : candies){
            if(num + k >= max){
                res.push_back(true);
            } else{
                res.push_back(false);
            }
        }
        return res;
    }
};
