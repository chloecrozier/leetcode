// https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        vector<int> change(3, 0);
        for(int i = 0; i < bills.size(); i++){
            if(bills[i] == 5){
                change[0] += 5;
            } else if(bills[i] == 10){
                change[1] += 10;
                change[0] -= 5;
            } else{
                change[2] += 20;
                if(change[1] >= 10){
                    change[0] -= 5;
                    change[1] -= 10;
                } else{
                    change[0] -= 15;
                }
            }
            if(change[0] < 0 || change[1] < 0 || change[2] < 0){
                return false;
            }
        }
        return true;
    }
};
