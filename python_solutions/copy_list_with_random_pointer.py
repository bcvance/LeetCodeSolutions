# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        cur = head
        node_map = {}
        while cur:
            node_map[cur] = Node(x=cur.val)
            cur = cur.next

        cur = head

        while cur:
            if cur.next:
                node_map[cur].next = node_map[cur.next]
            else:
                node_map[cur].next = None
            if cur.random:
                node_map[cur].random = node_map[cur.random]
            else:
                node_map[cur].random = None
            cur = cur.next

        return node_map[head]