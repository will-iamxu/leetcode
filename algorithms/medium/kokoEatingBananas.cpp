// Problem:
//     - int n: number of banana piles
//     - vector<int> piles: piles[i] represents the number of bananas in the i-th pile
//     - Koko has h hours before the guards return
//     - Goal: Find the minimum integer eating speed k such that Koko can eat all bananas in h hours

// Constraints:
//     - Koko eats from one pile per hour
//     - She eats up to k bananas per hour; if a pile has fewer than k, she finishes it in one hour
//     - She cannot split a pile across multiple hours or combine piles in one hour
//     - The maximum number of bananas she can eat in h hours at speed k is h * k

// Approach:
//     - Binary search on k (eating speed) between 1 and max(piles)
//     - For each candidate k, simulate how many hours it would take to finish all piles
//     - Use ceil(p / k) for each pile to calculate the time needed for that pile
//     - Find the smallest k such that the total time is <= h

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());  // Maximum possible k
        int res = r;

        while (l <= r) {
            int k = (l + r) / 2;

            long long totalTime = 0;
            for (int p : piles) {
                // Time to eat this pile at speed k
                totalTime += ceil(static_cast<double>(p) / k);
            }

            if (totalTime <= h) {
                // k is fast enough, try a slower one
                res = k;
                r = k - 1;
            } else {
                // k is too slow, try a faster one
                l = k + 1;
            }
        }
        return res;
    }
};
