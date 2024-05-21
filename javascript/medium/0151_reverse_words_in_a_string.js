// https://leetcode.com/problems/reverse-words-in-a-string/description/
var reverseWords = function(s) {
    return s.split(/\s+/).filter(Boolean).reverse().join(' ')
};
