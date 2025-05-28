// Given:
//     -array numbers: 1 indexed
//     - int target: target sum
// Constraints:
//     - One solution
//     - May not use same element twice (e.g right!=left)
// Approach:
//     - use two pointers to find target sum
//     - while right > target move right down 
//     - if right + left < target move right down
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size()-1;
        while (numbers[left] + numbers[right] != target && left < numbers.size() && right > 0){
            if (numbers[right] + numbers[left] > target){
                right--;
            }
            else {
                left++;
            }
        }
        return {left+1,right+1};
    }
};