// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/submissions/1347242546/
class Solution {
public:
    int minimumPushes(string word) {
        int length = word.length();
        if(length >= 24){
            if(length == 24){
                return 8 + 16 + 24;
            } else{
                return (8 + 16 + 24) + (4 * (length % 24));
            }
        } else if(length >= 16){
            if(length == 16){
                return 8 + 16;
            } else{
                return (8 + 16) + (3 * (length % 16));
            }
        } else if(length > 8){
            return 8 + (2 * (length % 8));
        } else{
            return length;
        }
    }
};
