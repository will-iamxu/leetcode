class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> inDeg(numCourses,0);
        vector<vector<int>> adj(numCourses);
        for (auto& p : prerequisites){
            int src = p[0];
            int dst = p[1];

            inDeg[dst]++;
            adj[src].push_back(dst);
        }

        queue<int> q;
        for (int i = 0; i < numCourses; ++i){
            if (inDeg[i] == 0){
                q.push(i);
            }
        }
        int finish = 0;
        vector<int> order;

        while (!q.empty()){
            int node = q.front();
            q.pop();
            order.push_back(node);
            finish++;
            for (auto& nb : adj[node]){
                inDeg[nb]--;
                if (inDeg[nb] == 0){
                    q.push(nb);
                }
            }
        }
        reverse(order.begin(), order.end());
        return finish == numCourses ? order : vector<int>{};
    }
};
