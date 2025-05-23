// Given:
//     - 2d 9x9 vector board: carries int from 0 to 9
//     - isValidSudoku: returns true if board is value, false otherwise
// Constraints:
//     - each row/column must only contain 1-9 without repition
//         -if board[row][column] isnt 1-9, return false
//     - each 3x3 subbox must also contain difits 1-9 without repition
// My approach
// 1) iterate through length n
// 2) create frequency maps for column, row, and subarray intialized to 0
// 3) increment the frequency maps based on the amount of times we see each number
// 4) if a the value for a key is greater than 1 return false
// 5) else validSudoku return true
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_map<char, int>> row(9), col(9), sub(9); //intializes frequency maps for all columns and rows and subarrays to 0

        for (int i = 0; i < 9; ++i){ //row
            for (int j = 0; j < 9; ++j){ //column
                char ch = board[i][j]; //current character
                if (ch == '.'){ //skip
                    continue;
                }
                if (ch < '1' || ch > '9'){  // not valid -> return false
                    return false; 
                }
                int subIdx = (i/3) * 3 + j/3; //calculating subIdx for subsquares, top left to bottom right
                row[i][ch]++; //for each character seen increment for row
                col[j][ch]++; //for column
                sub[subIdx][ch]++; //for subarray
                if (row[i][ch] > 1 || col[j][ch] > 1 || sub[subIdx][ch] > 1){ //greater than 0 at any of these points -> invalid
                    return false;
                }
            }
        }
        return true;
    }
};