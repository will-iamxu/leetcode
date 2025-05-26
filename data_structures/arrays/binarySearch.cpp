class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0; //low bounds 
        int high = nums.size() - 1; //high bounds 
        while (low<=high){ //makes sure search indexes inbetween low and high 
            int mid = low + (high - low)/2; //midpoint formula
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) { //if target greater, move low to be higher than mid
                low = mid + 1; 
                continue;
            }
            else if (nums[mid] > target){ //if target less, move high to be less than mid 
                high = mid - 1;
            }
        }
        return -1;
    }
};