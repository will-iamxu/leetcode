//Given:
//     -2d array matrix: sorted increasing order
//     -int target
//     -searchMatrix: returns true if target is in matrix, false otherwise
// Constraints:
//     - None
// Approach:
//     - Binary Search
//         - Standard binary search on an array of sorted is as follows
//             - if num > mid -> right side, if num < mid left side 
//         - Have to use different way to calculate mid 
//     - Converting the grid into a normal array -> m*n-1 is length
//     - Need to convert back to grid
//         - mid = (low + high / 2)
//         - Ex: index 2 -> 3*1-1 m = 3, n = 1 
//             - row = mid/n
//             - col = mid%n

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int low = 0;
        int high = n * m - 1;
        while (low <= high){
            int mid = (low+high)/2;
            int row = mid/n;
            int col = mid%n;
            if (matrix[row][col] == target) return true;
            else if (matrix[row][col] < target){
                low = mid + 1;
            }
            else{
                high = mid-1;
            }
        }
        return false;
    }
};