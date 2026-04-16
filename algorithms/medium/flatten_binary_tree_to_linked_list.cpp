class Solution {
public:
    void flatten(TreeNode* root) {
        TreeNode* node = root;

        while (node){
            if (node->left){
                TreeNode* rightM = node->left;
                while (rightM->right){
                    rightM = rightM->right;
                }
                rightM->right = node->right;
                node->right = node->left;
                node->left = nullptr;
            }
            node = node->right;
        }
    }
};
