class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        int res = 0;
        deque<pair<TreeNode*, long long>> q = {{root,0}};

        while (!q.empty()){
            int size = q.size();
            long long leftM = q.front().second;
            long long rightM = q.back().second;
            res = max(res, (int)(rightM - leftM) + 1);

            for (int i = 0; i < size; ++i){
                auto [node, pos] = q.front();
                q.pop_front();

                long long offset = pos - leftM;
                if (node->left) q.push_back({node->left, 2 * offset});
                if (node->right) q.push_back({node->right, 2 * offset + 1});

            }
        }
        return res;
    }
};
