from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqSet = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqSet[course].append(prereq)
        order = []
        
        seen = set()
        
        def dfs(course):
            if course in seen:
                return False
            if prereqSet[course] == []: 
                if course not in order:
                    order.append(course)
                return True

            seen.add(course)
            for prereq in prereqSet[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            prereqSet[course] = []
            if course not in order:
                order.append(course)
            return True


        for course in prereqSet:
            if not dfs(course):
                return []
            elif len(order) == numCourses:
                return order      
