class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
