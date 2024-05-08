// https://leetcode.com/problems/valid-parentheses/description/
class Solution {
public:
    bool isStart(char c){
        if(c == '(' || c == '{' || c == '['){
            return true;
        }
        return false;
    }

    bool matches(char c1, char c2){
        if(c1 == '(' && c2 == ')'){
            return true;
        } else if(c1 == '{' && c2 == '}'){
            return true;
        } else if(c1 == '[' && c2 == ']'){
            return true;
        }
        return false;
    }

    bool isValid(string s) {
        vector<char> stack;
        for(char c : s){
            if(isStart(c)){
                stack.push_back(c);
            } else{
                if(stack.size() == 0){
                    return false;
                }
                if(!matches(stack.back(), c)){
                    return false;
                }
                stack.pop_back();
            }
        }

        if(stack.size() == 0){
            return true;
        }
        return false;
    }
};
