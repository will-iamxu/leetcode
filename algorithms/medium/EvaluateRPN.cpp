// Given:
//     -vector tokens: string of numbers and operators
//     -evalRPN: evaluates Reverse Polish Notation
//         - RPN: operators follow operands
// Constraints:
//     -only valid operators: '+', '-', '*', '/'
//     -division between two ints trunactes toward 0
//     -no division by 0
// Approach:
//     -if number, push to stack
//     -else perform operation between previous two operands
//     -need to convert string to number 
#include <ctype.h>
#include <stack>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        int num1;
        int num2;
        int temp;
        for (int i = 0; i<tokens.size(); ++i){
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "/" && tokens[i] != "*"){
                s.push(stoi(tokens[i])); //string to integer
            }
            else{
                if (tokens[i] == "+"){
                    num1 = s.top();
                    s.pop();
                    num2 = s.top();
                    s.pop();
                    s.push(num1+num2);
                }
                else if (tokens[i] == "*"){
                    num1 = s.top();
                    s.pop();
                    num2 = s.top();
                    s.pop();
                    s.push(num2*num1);
                }    
                else if (tokens[i] == "/"){
                    num1 = s.top();
                    s.pop();
                    num2 = s.top();
                    s.pop();
                    s.push(num2/num1);                    
                }
                else if (tokens[i] == "-"){
                    num1 = s.top();
                    s.pop();
                    num2 = s.top();
                    s.pop();
                    s.push(num2-num1);                    
                }
            }
        }
        return s.top();
    }
};