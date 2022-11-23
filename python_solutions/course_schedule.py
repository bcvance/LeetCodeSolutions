from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        prereq_map = {}
        num_can_take = numCourses
        print(num_can_take, numCourses)
        for course, prereq in prerequisites:
            if course in prereq_map:
                prereq_map[course].append(prereq)
            else:
                prereq_map[course] = [prereq]
        

        def dfs(course, seen):
            if course in seen:
                return False
            if course not in prereq_map or prereq_map[course] == []:
                return True
            seen.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq, seen):
                    return False
            seen.remove(course)
            prereq_map[course] = []
            return True

        for course in prereq_map:
            if not dfs(course, set()):
                return False
        return True
            