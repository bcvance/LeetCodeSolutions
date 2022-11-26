class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        cur = head
        prev = None

        while True:
            old_next = cur.next
            cur.next = prev
            prev = cur
            if not old_next:
                break
            cur = old_next
        return cur
