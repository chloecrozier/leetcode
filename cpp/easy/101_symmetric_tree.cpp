// https://leetcode.com/problems/symmetric-tree/description/
class Solution {
public:
    bool compareVals(TreeNode* p, TreeNode* q){
        if(p == NULL && q == NULL){
            return true;
        } else if(p == NULL || q == NULL){
            return false;
        } else {
            if(p->val == q->val){
                bool outwards = compareVals(p->left, q->right);
                bool inwards = compareVals(p->right, q->left);
                return inwards && outwards;
            }
        }
        return false;
    }

    bool isSymmetric(TreeNode* root) {
        if(root != NULL){
            return compareVals(root->left, root->right);
        }
        return true;
    }
};
