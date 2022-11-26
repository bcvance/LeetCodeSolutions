class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
            
        cur = head
        array = []
        length = 0

        while cur:
            length += 1
            array.append(cur)
            cur = cur.next

        n = 0
        cur = head
        even = True
        while cur and n < length:
            if even:
                cur.next = array[length-1-n]
                array[length-1-n] = None
                n += 1
            else:
                cur.next = array[n]
                array[n] = None
            even = not even
            cur = cur.next

        