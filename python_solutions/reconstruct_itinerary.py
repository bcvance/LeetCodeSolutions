from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacency_matrix = {}
        itinerary = ["JFK"]
        tickets.sort()
        for orig, dest in tickets:
            if orig in adjacency_matrix:
                adjacency_matrix[orig].append(dest)
            else:
                adjacency_matrix[orig] = [dest]

        def dfs(origin):
            if len(itinerary) == len(tickets)+1:
                return True
            if origin not in adjacency_matrix:
                return False
            temp = adjacency_matrix[origin]
            for i, v in enumerate(temp):
                itinerary.append(v)
                adjacency_matrix[origin].pop(i)
                if dfs(v): return True
                itinerary.pop()
                adjacency_matrix[origin].insert(i, v)
            return False

        dfs("JFK")

        return itinerary