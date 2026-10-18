class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_hash = {i: [] for i in range(numCourses)}

        for prereq in prerequisites:
            if prereq[0] in prereq_hash:
                prereq_hash[prereq[0]].append(prereq[1])
            else:
                prereq_hash[prereq[0]] = [prereq[1]]

        def dfs(prereq_hash, visited, curr_course):
            if visited and curr_course in visited:
                return False
            elif not prereq_hash[curr_course]:
                return True
            else:
                visited.append(curr_course)
                for prereq in prereq_hash[curr_course]:
                    if not dfs(prereq_hash, visited, prereq):
                        return False
                prereq_hash[curr_course] = []
                visited.pop()
                    
                return True
        
        for i in range(numCourses):
            if not dfs(prereq_hash, [], i):
                return False
        return True
