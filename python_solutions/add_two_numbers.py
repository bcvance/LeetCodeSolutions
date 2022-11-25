class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        res_head = ListNode()
        cur = res_head
        carry = 0
        while l1 or l2:
            cur.next = ListNode()
            cur = cur.next
            if l1 and l2:
                total = l1.val + l2.val + carry
                cur.val = total % 10
                carry = total // 10
            
                l1 = l1.next
                l2 = l2.next
            elif not l2:
                cur.val = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                
                l1 = l1.next
            elif not l1:
                cur.val = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10

                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(val=carry)
            
        return res_head.next
        
