// https://leetcode.com/problems/design-parking-system/description/
class ParkingSystem {
public:
    int b;
    int m;
    int s;
    ParkingSystem(int big, int medium, int small) {
        b = big;
        m = medium;
        s = small;
    }
    
    bool addCar(int carType) {
        if(carType == 1){
            if(b){
                b--;
                return true;
            }
        } else if(carType == 2){
            if(m){
                m--;
                return true;
            }
        } else{
            if(s){
                s--;
                return true;
            }
        }
        return false;
    }
};
