// https://leetcode.com/problems/add-binary/description/
class Solution {
public:
    string addBinary(string a, string b) {

        if(a.length() < b.length()){
            string temp = a;
            a = b;
            b = temp;
        }

        int indexA = a.length() - 1;
        int indexB = b.length() - 1;

        while(indexA >= 0 && indexB >= 0){
            cout << a << endl;
            if(a[indexA] == '1' && b[indexB] == '1'){
                a[indexA] = '0';
                for(int i = indexA - 1; i >= 0; i--){
                    if(a[i] == '0'){
                        a[i] = '1';
                        i = -1;
                    } else{
                        a[i] = '0';
                    }
                }
                if(a[0] == '0'){
                    a = "1" + a;
                    indexA++;
                }
            } else if(a[indexA] != b[indexB]){
                a[indexA] = '1';
            } else{
                a[indexA] = '0';
            }
            indexA--;
            indexB--;
        }
        return a;
    }
};
