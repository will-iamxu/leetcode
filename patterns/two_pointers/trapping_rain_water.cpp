class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = height.size()-1;
        int rMax = height[r], lMax = height[0];
        int res = 0;
        while (l < r){
            if (lMax < rMax){
                l++;
                lMax = max(lMax, height[l]);
                res += lMax - height[l];
            }
            else{
                r--;
                rMax = max(rMax, height[r]);
                res += rMax - height[r];
            }
        }
        return res;
    }
};
