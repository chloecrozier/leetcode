// https://leetcode.com/problems/add-strings/solutions/4192041/basic-c-code-beats-100/
class Solution {
public:
    string addStrings(string num1, string num2) {
        string res;
        string addedNum;
        if(num1.length() > num2.length()){
            res = num1;
            addedNum = num2;
        } else{
            res = num2;
            addedNum = num1;
        }
        int index = res.length() - 1;
        int carryOver = 0;
        for(int i = 0; i < addedNum.length(); i++){
            int sum = carryOver + res[index] - '0' + addedNum[addedNum.length() - i - 1] - '0';
            if(sum > 9){
                res[index] = sum % 10 + '0';
                carryOver = 1;
            } else{
                res[index] = sum + '0';
                carryOver = 0;
            }
            index--;
        }
        if(carryOver > 0){
            if(index <= 0){
                if(index == 0){
                    if(res[index] == '9'){
                        res[index] = '0';
                        res = "1" + res;
                    } else{
                        res[index]++;
                    }
                } else{
                    res = "1" + res;
                }
            } else{
                if(res[index] == '9'){
                    while(res[index] == '9' && index > 0){
                        res[index] = '0';
                        index--;
                    }
                    if(res[index] == '9'){
                        res[index] = '0';
                        res = "1" + res;
                    } else{
                        res[index]++;
                    }
                } else{
                    res[index]++;
                }
            }
        }
        return res;
    }
};
