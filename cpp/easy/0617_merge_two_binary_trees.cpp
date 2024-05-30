// https://leetcode.com/problems/merge-two-binary-trees/description/
class Solution {
public:
    TreeNode* traverseTree(TreeNode* root, TreeNode* root1, TreeNode* root2){
        if(root1 != NULL && root2 == NULL){
            root = new TreeNode(root1->val);
            root->right = root1->right;
            root->left = root1->left;
        }
        if(root1 == NULL && root2 != NULL){
            root = new TreeNode(root2->val);
            root->right = root2->right;
            root->left = root2->left;
        }
        if(root1 != NULL && root2 != NULL){
            root = new TreeNode(root1->val + root2->val);
            root->right = traverseTree(NULL, root1->right, root2->right);
            root->left = traverseTree(NULL, root1->left, root2->left);
        }
        return root;
    }

    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        TreeNode* root = traverseTree(NULL, root1, root2);
        return root;
    }
};
