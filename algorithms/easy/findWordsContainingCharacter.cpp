// Given:
//     -array string words
//     -char x
// Return:
//     -array of indices representing words that contain character x
// Approach:
//     -iterate through words
//     -iterate through the word, if x is in word append to solution
//     -return solution
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        int wordsLength = words.size();
        vector<int> res;
        for (int i = 0; i < wordsLength; ++i){
            string cur = words[i];
            int n = cur.size();
            for (int j = 0; j < n; ++j){
                if (cur[j] == x) {
                    res.push_back(i);
                    break;
                }
            }
        }
        return res;
    }
};