// Given:
//     -int n: pairs of parenthesis
//     -generateParenthesis: generates all combinations of wellformed parenthesis
//         - aka every parathesis must be closed and cannot be left open
// Constraints:
//     - well-formed
//         - e.g cant be )(
//         - ) cannot be greater than (
//     - cant have more parenthesis than pairs
//         - n = 3, can't have more than 3 (
// Approach:
//     - Backtracking
//     - only add ( if ( count < n
//     - only add ) if ) count < ( count
//     - only valid if ( and ) count == n
// 1) checks if at a valid state
// 2) if not, it tries adding (
// 3) then backtracks with push_back
// 4) then tries adding )
// 5) then backtracks again
// 6) done exploring down a state, return and exit
class Solution {
public:
    void backtrack(int open, int close, int n, vector<string>& res, string& stack){
        if (open == close && open == n){
            res.push_back(stack);
            return;
        }
        if (open < n){
            stack += '('; 
            backtrack(open+1,close,n,res,stack);
            stack.pop_back(); //goes back after exploring depth for other possibilities
        }
        if (close < open){
            stack += ')';
            backtrack(open, close+1,n,res,stack);
            stack.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string stack;
        backtrack(0,0,n,res,stack);
        return res;
    }
};