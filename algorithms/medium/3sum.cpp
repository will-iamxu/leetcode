// Given:
//     -array int nums
//     -array of array threeSum: returns distinct triplets that add to 0
// Constraints:
//     - no duplicates
//     - sum is equal to 0
//     - order doesn't matter
// Approach:
//     - iterate through list as first numbers
//     - use two pointers for other two numbers to find the other two numbers
//     - append all numbers to list
//     - return list of lists
#include <vector>
#include <algorithm>

using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> sol; //solution to hold
        sort(nums.begin(), nums.end());  //sort nums to properly use 2 pointer
        for (int i = 0; i < nums.size(); ++i){ 
            if (i > 0 && nums[i] == nums[i - 1]) continue; //skip repeat numbers
            int target = 0 - nums[i]; //makes it so we have a target for 2 pointer
            int left = i + 1;
            int right = nums.size()-1;
            while (left < right){ 
                if (nums[left] + nums[right] == target){
                    sol.push_back({nums[i], nums[left], nums[right]});
                
                    while (left < right && nums[left] == nums[left + 1]) ++left; //skip duplicates
                    while (left < right && nums[right] == nums[right - 1]) --right; 

                    ++left;
                    --right;
                } 
                else if (nums[left] + nums[right] < target) {
                    ++left;
                    } 
                else {
                    --right;
                }
            }
        }
        return sol;
    }
};