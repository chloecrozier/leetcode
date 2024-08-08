// https://leetcode.com/problems/integer-to-english-words/description/?envType=daily-question&envId=2024-08-07
class Solution {
public:
    vector<string> singleDigit{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<string> doubleDigitTeen{"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    vector<string> doubleDigitTens{"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    vector<string> places{"", "", "Thousand", "Million", "Billion"};

    string getChunk(string chunk){
        string res = "";
        bool isTeen = false;
        if(chunk.length() == 3){
            for(int i = 0; i < chunk.length(); i++){
                if(i == 0){
                    // gets first digit of 1XX, 2XX, etc
                    if(chunk[i] != '0'){
                        res += singleDigit[chunk[i] - '0'] + " Hundred";
                    }
                } else if(i == 1){
                    if(chunk[i] != '0'){
                        // if teens
                        if(chunk[i] - '0' < 2){
                            isTeen = true;
                        } else{
                            // if 2X, 3X, etc
                            if(chunk.substr(0,1) == "0"){
                                res += doubleDigitTens[(chunk[i] - '0') - 2];
                            } else{
                                res += " " + doubleDigitTens[(chunk[i] - '0') - 2];
                            }
                        }
                    }
                } else{
                    if(isTeen){
                        // add the teen num based on second digit
                        if(chunk.substr(0,1) == "0"){
                            res += doubleDigitTeen[chunk[i] - '0'];
                        } else{
                            res += " " + doubleDigitTeen[chunk[i] - '0'];
                        }
                    } else{
                        // if not 20, 30, etc
                        if(chunk[i] != '0'){
                            if(chunk.substr(0, 2) == "00"){
                                res += singleDigit[chunk[i] - '0'];
                            } else{
                                res += " " + singleDigit[chunk[i] - '0'];
                            }
                        }
                    }
                }
            }
        } else if(chunk.length() == 2){
            for(int i = 0; i < chunk.length(); i++){
                if(i == 0){
                    if(chunk[i] != '0'){
                        // if teens
                        if(chunk[i] - '0' < 2){
                            isTeen = true;
                        } else{
                            // if 2X, 3X, etc
                            res += doubleDigitTens[(chunk[i] - '0') - 2];
                        }
                    }
                } else{
                    if(isTeen){
                        // add the teen num based on second digit
                        res += doubleDigitTeen[chunk[i] - '0'];
                    } else{
                        // if not 20, 30, etc
                        if(chunk[i] != '0'){
                            if(chunk.substr(0, 1) == "0"){
                                res += singleDigit[chunk[i] - '0'];
                            } else{
                                res += " " + singleDigit[chunk[i] - '0'];
                            }
                        }
                    }
                }
            }
        } else{
            return res += singleDigit[chunk[0] - '0'];
        }
        return res;
    }

    string numberToWords(int num) {
        string numString = to_string(num);
        string res = "";
        bool isFirstChunk = true;
        int greatestChunk = numString.length() % 3;
        int numChunks;
        if(greatestChunk == 0){
            numChunks = (numString.length() / 3);
        } else{
            numChunks = 1 + (numString.length() / 3);
        }
        
        if(greatestChunk != 0){
            res += getChunk(numString.substr(0, greatestChunk));
            if(numChunks > 1){
                res += " " + places[numChunks] + " ";
            }
            numChunks--;
            isFirstChunk = false;
        }
        while(numChunks > 0){
            string chunk =  numString.substr(greatestChunk, 3);
            res += getChunk(chunk);
            if(numChunks > 1 && chunk != "000"){
                res += " " + places[numChunks] + " ";
            }
            greatestChunk += 3;
            numChunks--;
            if(chunk == "000" && numChunks == 0){
                res = res.substr(0, res.length() - 1);
            }
        }
        return res;
    }
};
