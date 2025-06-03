// Given:
//     - int array prices: price of stock on ith day
//     - int maxProfit: maximize profit by choosing a day to buy stock and a day to sell
// Constraints:
//     - buy day has to be before sell day  r>l
// Approach:
//     - Sliding window, while r<prices.size()
//         - max is prices[left]-prices[right]
//         - if prices[left] > prices[right] -> move left to right 
//         - if prices[left] < prices[right], subtract and compare that price to current max 
 
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int right = 1;
        int maxP = 0;
        while (right < prices.size()){
            if (prices[left] < prices[right]){
                int currProfit = prices[right] - prices[left];
                maxP = max(maxP, currProfit);
            }
            else{
                left = right;
            }
            ++right;
            
        }
        return maxP;
    }
};