// Given: 
//     - array int nums
//     - productExceptSelf: returns int vector
//         -vector[i] is equal to product of all elements in nums except nums[i]
// Constraints:
//     - fits in 32-bit integer
//     - O(n) time
//     - cannot use division operator e.g. multiplying nums out then dividing by each nums[i] to fill out solution vector

// Initial Thoughts:
//     - Brute force: two loops for every vector[i] loop through subarray and multiple elements together and place into a solution vector at index [i] -> O(n^2)
// Approach:
//     - Use prefix and postfix arrays
//     - prefix: multiplication of numbers before vector[i]
//     - postfix: multiplication of numbers after vector[i]
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size(); //size of nums
        vector<int> sol(n,1); //intialized vector length n to hold solution
        for (int i = 0; i < n-1; ++i){ //calculates prefix for each slot
            sol[i+1] *= sol[i]*nums[i]; //each prefix = prefix before * nums before index
        }
        int prev = 1; //tracking variable to hold for suffix
        for (int i = n-1; i>=0; --i){ //looping backwards 
            sol[i] *= prev; //solution at i is equal to suffix * stored prefix
            prev *= nums[i]; //update suffix for next number
        }
        return sol;
    }
};