// https://leetcode.com/problems/sqrtx/description/
class Solution {
public:
    int mySqrt(int x) {
        int left = 1;
        int right = x;
        int mid = 0;

        if(x == 0){
            return mid;
        }

        while(left <= right){
            mid = left + (right - left) / 2;

            if(mid == x / mid){
                return mid;
            } else if(mid > x / mid){
                right = mid - 1;
            } else{
                left = mid + 1;
            }
        }
        return right;
    }
};
