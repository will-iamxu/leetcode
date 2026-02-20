class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses
        for nxt, pre in prerequisites:
            inDegree[nxt] += 1
            adj[pre].append(nxt)

        res = []
        def dfs(node):
            res.append(node)
            inDegree[node] -= 1
            for nei in adj[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    dfs(nei)
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                dfs(i)
        
        return res if numCourses == len(res) else []