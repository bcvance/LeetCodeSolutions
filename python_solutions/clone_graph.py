from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        visited = set()
        q = deque()
        q.append(node)

        node_map = {}
        
        def bfs():
            while q:
                node = q.pop()
                visited.add(node)
                new_node = Node(val=node.val)
                node_map[node] = new_node

                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
        bfs()
        for k, v in node_map.items():
            for neighbor in k.neighbors:
                v.neighbors.append(node_map[neighbor])
        return node_map[node]

            
