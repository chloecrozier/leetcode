// https://leetcode.com/problems/insert-interval/description/?envType=daily-question&envId=2024-08-12
class Solution {
public:
    // helper functions to find if the new interval intersects with an exisiting interval
    bool inInterval(vector<int>& interval, int lVal, int hVal){
        if(lVal <= interval[1] && hVal >= interval[0]){
            return true;
        }
        return false;
    }

    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int lVal = newInterval[0];
        int lIndex = 0;
        bool lAbove = false;
        int hVal = newInterval[1];
        int hIndex = 0;
        bool hAbove = false;

        // new interval is the smallest interval
        if(intervals.size() > 0 && hVal < intervals[0][0]){
            res.push_back(newInterval);
            for(int i = 0; i < intervals.size(); i++){
                res.push_back(intervals[i]);
            }
        }
        // new interval is the largest interval
        else if(intervals.size() > 0 && lVal > intervals[intervals.size() - 1][1]){
            for(int i = 0; i < intervals.size(); i++){
                res.push_back(intervals[i]);
            }
            res.push_back(newInterval);
        }
        else{
            for(int i = 0; i < intervals.size(); i++){
                // add all exisitng intervals outside of the new interval range
                if(!inInterval(intervals[i], lVal, hVal)){
                    res.push_back(intervals[i]);
                }

                if(lVal > intervals[i][1]){
                    lIndex++;
                }
                if(hVal >= intervals[i][0]){
                    hIndex++;
                }
            }
            // if new interval is not between existing intervals
            if(lIndex == hIndex){
               res.insert(res.begin() + lIndex, newInterval);
            } else{
                // find range of newly created interval
                if(lVal > intervals[lIndex][0]){
                    newInterval[0] = intervals[lIndex][0];
                }
                if(hVal < intervals[hIndex - 1][1]){
                    newInterval[1] = intervals[hIndex - 1][1];
                }
                res.insert(res.begin() + lIndex, newInterval);
            }
        }
        return res;
    }
};
