# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        head1 = head2 = None
        tail1 = tail2 = None
        curr_node = head
        while curr_node:
            if curr_node.val < x:
                if head1 == None:
                    head1 = curr_node
                    tail1 = curr_node
                else:
                    tail1.next = curr_node
                    tail1 = tail1.next

            else:
                if head2 == None:
                    head2 = curr_node
                    tail2 = curr_node
                else:
                    tail2.next = curr_node
                    tail2 = tail2.next

            curr_node = curr_node.next

        if head2 == None:
            return head1
        
        if head1 == None:
            return head2

        tail1.next = head2
        tail2.next = None

        return head1
