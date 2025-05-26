// Given:
//     -string s: sentence
//     -bool isPalindrome: checks is palidrome
// Constraints:
//     -letters and numbers
//         -<cctype> isalum
//     -spaces and other characters are skipped
//     - caps dont matter tolower(s)
// Intial Thoughts:
//     -two pointer
//     -iterate through string 
//         -checking if left = right
//         -if left != right return false
//         -does not need to iterate through entire string, only half is sufficient
// Edge Cases:
//     - middle character -> can be skipped doesn't matter 
//         -detemined by odd or even length string
// Worked Example:
// s = race car
// 1) remove spaces -> <algorithm> s.erase(std::remove(s.begin(), s.end(), ' '), s.end())
// 2) left = i, right = size - i
// 3) if odd (s&1 == 1) -> i iterates to i-size/2
// 4) if even -> i iterates to size/2
// 5) move pointers and check each value
// 6) if not same value return false
#include <cctype>
#include <algorithm>
#include <string>
class Solution {
public:
    bool isPalindrome(string s) {
        s.erase(std::remove(s.begin(), s.end(), ' '), s.end()); //erases whitespace
        int l = 0; //left pointer
        int r = s.size()-1; //right pointer 
        while (l < r){
            while (l < r && !isalnum(s[l])) ++l; //makes sure doesnt go out of bounds and makes sure if its not alphanum it increments left
            while (l < r && !isalnum(s[r])) --r; //makes sure doesnt go out of bounds and makes sure if its not alphanum it increments right
            if (tolower(s[l]) != tolower(s[r])) return false; //if lower values dont match, then not palindrome 
            ++l; //increment 
            --r;
        }
        return true;
    }
};