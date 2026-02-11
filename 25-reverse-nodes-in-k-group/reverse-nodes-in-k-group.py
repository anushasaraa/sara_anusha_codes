# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        tk = k
        prev = None
        first = True

        while curr:
            if tk == k:
                firstNode = curr

            tempNode = curr.next
            curr.next = prev

            prev = curr
            curr = tempNode

            tk -= 1

            if tk == 0:
                if first:
                    first = False
                    res = prev
                else:
                    temp.next = prev
                temp = firstNode
                tk = k

                firstNode.next = curr
                prev = None
            
        if tk != 0:
            prev2 = None
            while prev:
                tempNode = prev.next
                prev.next = prev2

                prev2 = prev
                prev = tempNode
            
            temp.next = prev2

        return res
        