# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
     # Dummy node to start the merged list
        head = point = ListNode(0)
        
        while True:
            min_index = -1
            min_value = float('inf')
            # Find the list with the smallest head node
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i
            # If all lists are empty, break
            if min_index == -1:
                break
            # Append the smallest node to the merged list
            point.next = lists[min_index]
            point = point.next
            # Move the pointer in the selected list forward.
            # This does NOT move nodes between lists A and B;
            # it simply advances the pointer in the original list (e.g., list A),
            # so the next node from that list will be considered in future iterations.
            lists[min_index] = lists[min_index].next
        
        return head.next     
