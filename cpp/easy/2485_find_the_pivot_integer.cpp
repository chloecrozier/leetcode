// https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-08-07
class Solution {
public:
    int pivotInteger(int n) {
        int leftIndex = 1;
        int rightIndex = n;
        int leftSum = 1;
        int rightSum = n;
        if(leftIndex == rightIndex){
            return leftIndex;
        }
        while(leftIndex != rightIndex){
            if(leftSum < rightSum){
                leftSum += ++leftIndex;
            } else{
                rightSum += --rightIndex;
            }
        }
        if(rightSum == leftSum){
            return leftIndex;
        } else{
            return -1;
        }
    }
};
