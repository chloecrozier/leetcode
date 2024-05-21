// Posted Solution: https://leetcode.com/problems/range-sum-of-bst/solutions/5176977/recursive-c-approach-beats-97-of-times/
// https://leetcode.com/problems/range-sum-of-bst/description/
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root == NULL){
            return 0;
        }
        if(root->val >= low && root->val <= high){
            return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
        } else if(root->val > high){
            return rangeSumBST(root->left, low, high);
        } else if(root->val < low){
            return rangeSumBST(root->right, low, high);
        } else{
            return 0;
        }
    }
};
