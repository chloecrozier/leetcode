// https://leetcode.com/problems/same-tree/description/
class Solution {
public:
    void traverseTrees(TreeNode* p, TreeNode* q, bool* equals){
        if(p != NULL && q != NULL){
            if(p->val != q->val){
                *equals = false;
            }
            traverseTrees(p->left, q->left, equals);
            traverseTrees(p->right, q->right, equals);
        } else if(p == NULL && q != NULL || p != NULL && q == NULL){
            *equals = false;
        }
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool equals = true;
        traverseTrees(p, q, &equals);
        return equals;
    }
};
