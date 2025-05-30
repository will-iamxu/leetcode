// Given: 
//     - array temperature: integers
//     - array dailyTemperature: the number of days you have to wait to get a warmer temperature
// Constraints:
//     - If there is no future day available, answer[i] = 0
// Approach:
//     - monotomic stack to store indexes
//     - when current temp is warmer than index at top of stack change index in ans to current day - waited day


class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int len = temperatures.size();
        vector<int> ans (len, 0);
        stack<int> idx;
        for (int i = 0; i < temperatures.size(); ++i){
            while (!idx.empty() && temperatures[i] > temperatures[idx.top()]){ //continuosly checks until a warmer temp index is found 
                int prev = idx.top(); //last coldest day
                idx.pop();
                ans[prev] = i - prev;
            }
            idx.push(i); //if not warmer, push
        }
        return ans;
    }
};