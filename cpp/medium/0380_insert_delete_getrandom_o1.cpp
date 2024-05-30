// https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
class RandomizedSet {
    private:
        vector<int> set;
        unordered_map<int, int> map;
public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        if(map.count(val) > 0){
            return false;
        } else{
            map[val] = set.size();
            set.push_back(val);
            return true;
        }
    }
    
    bool remove(int val) {
        if(map.count(val) == 0){
            return false;
        } else{
            int lastVal = set[set.size() - 1];
            map[lastVal] = map[val];
            set[map[val]] = lastVal;
            set.pop_back();
            map.erase(val);
            return true;
        }
    }
    
    int getRandom() {
        return set[rand() % set.size()];
    }
};
