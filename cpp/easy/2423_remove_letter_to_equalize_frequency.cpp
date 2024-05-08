// https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/
class Solution {
public:
    bool equalFrequency(string s) {
        map<char, int> letters;
        map<int, int> counts;

        // get the frequency of each letter in s
        for(int i = 0; i < s.length(); i++){
            letters[s[i]]++;
        }

        // get the frequency of each letter frequency
        for(auto item : letters){
            counts[item.second]++;
        }

        // if each letter has the same number of occurances (aazz)
        if(counts.size() == 1){
            // ex. (abcd)
            if(counts.begin()->first == 1){
                return true;
            }
            // ex. (aaa)
            else if(counts.begin()->second == 1){
                return true;
            }
            // ex. (aazz)
            else{
                return false;
            }
        } 
        // if there are two different occurance frequencies
        else if(counts.size() == 2){
            auto start = counts.begin();
            auto end = start++;

            // if there is one letter occuring once (abbcc)
            if(start->second ==  1){
                // ex. (aab)
                if(start->first - end->first == 1){
                    return true;
                }
                // ex. (abb)
                if(start->first ==  1 && start->second == 1){
                    return true;
                }
            } 
            // if there is one letter occuring once (aabbc)
            if(end->second == 1){
                // ex. (abb)
                if(end->first - start->first == 1){
                    return true;
                }
                // ex. (aab)
                if(end->first ==  1 && end->second == 1){
                    return true;
                }
            }
        }
        // if there are letter occurring at more than two frequencies
        else{
            return false;
        }
        return false;
    }
};
