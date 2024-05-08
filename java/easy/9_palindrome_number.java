// https://leetcode.com/problems/palindrome-number/
class Solution {
    public boolean isPalindrome(int x) {
        String newNum = "";
        char letter;
        String num = Integer.toString(x);
        int length = num.length();
        for (int i = 0; i < length; i++) {
            letter = num.charAt(i);
            newNum = letter + newNum;
        }
        if (newNum.equals(num)) {
            return true;
        } else{
            return false;
        }        
    }
}
