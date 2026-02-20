class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        visited = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visiting.add(crs)

            for nc in preMap[crs]:
                if not dfs(nc):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True