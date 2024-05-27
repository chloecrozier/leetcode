// Posted Solution: https://leetcode.com/problems/deepest-leaves-sum/solutions/5213624/simple-recursive-dfs-c-approach-beats-96-of-times/
// https://leetcode.com/problems/deepest-leaves-sum/description/
class Solution {
public:
    int getDepth(TreeNode* root){
        if(root == NULL){
            return 0;
        } else{
            return max(getDepth(root->left), getDepth(root->right)) + 1;
        }
    }
    int getSum(TreeNode* root, int maxDepth, int currDepth){
        if(root == NULL){
            return 0;
        } else{
            if(maxDepth == currDepth + 1){
                return root->val;
            } else{
                return getSum(root->left, maxDepth, currDepth + 1) + getSum(root->right, maxDepth, currDepth + 1);
            }
        }
    }
    int deepestLeavesSum(TreeNode* root) {
        return getSum(root, getDepth(root), 0);
    }
};
