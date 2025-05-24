// Given:
//     - int array nums: unsorted
//     - longestConsective: returns length of longest consectuve elements
// Constraints:
//     - O(n) time
//     - same values are not considered consecutive -> use a set in some way
// Initial thoughts:
//     - what makes a number part of a sequence is if it is +-1 from a different number 
//     - frequency map that iterates over longest sequence
//         - if nums[i]+-1 isnt on map, add to map
//         - if nums[i]+-1 is on map, add to that number to array index
//             -expand the map key and increment length

#include <unordered_map>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0;

        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if (mp.count(num)) continue; //skips if seen
            int left = 0;
            if (mp.count(num - 1)) { // count(num - 1) returns 1 if (num - 1) exists in the map
                left = mp[num - 1]; //if exists get length of left sequence
            }
            int right = 0;
            if (mp.count(num + 1)) { // mp.count(num + 1) returns 1 if (num + 1) exists in the map
                right = mp[num + 1]; //if exists get length of right sequence
            }
            int length = left + right + 1; //length of new sequence + num
            mp[num] = length; //store at current number
            // Update boundaries
            mp[num - left] = length; //update left boundary
            mp[num + right] = length; //update right boundary
            res = max(res, length); //result 
        }

        return res;
    }
};
