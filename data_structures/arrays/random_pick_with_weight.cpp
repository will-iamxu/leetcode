class Solution {
public:
    vector<int> pre;
    int l, r;
    Solution(vector<int>& w) {
        pre.push_back(0);
        for (auto& wg: w){
            pre.push_back(pre.back() + wg);
        }
    }

    int pickIndex() {
        double target = pre.back() * ((double)rand() / RAND_MAX);
        l = 1, r = pre.size()-1;
        while (l < r){
            int m = (l+r)/2;
            if (pre[m] > target){
                r = m;
            }
            else {
                l = m + 1;
            }
        }
        return l -1;
    }
};
