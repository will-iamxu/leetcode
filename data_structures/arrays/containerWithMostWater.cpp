// Given:
//     -array height: length n, full of integers representing various heights
//     -maxArea: returns maxArea height * width
// Constraints:
//     - None
// Approach:
//     - Two pointers approach
//     - use temp variable to hold max 
class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        int left = 0;
        int right = height.size() - 1;
        int minHeight = 0;
        while(left<right){
            int tempArea;
            int width = right-left;
            if (height[left] > height[right]){
                tempArea = height[right] * width;
                if (tempArea > max) max = tempArea;
                --right;
            }
            else {
                tempArea = height[left] * width;
                if (tempArea > max) max=tempArea;
                ++left;
            }
        }
        return max;
    }
};