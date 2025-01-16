// https://leetcode.com/problems/to-be-or-not-to-be/description/?envType=study-plan-v2&envId=30-days-of-javascript
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: (testVal) => {
            if(val === testVal){
                return true
            } else{
                throw new Error("Not Equal")
            }
        },
        notToBe: (testVal) => {
            if(val === testVal){
                throw new Error("Equal")
            } else{
                return true
            }
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
