class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        cur = head

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            elif not list2:
                while list1:
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
            elif not list1:
                while list2:
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
        return head.next
