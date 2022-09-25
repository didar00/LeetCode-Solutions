# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        info = list()
        
        node = head
        while node:
            info.append([node.val, node])
            node = node.next
        
        size = len(info)
        if size == 1:
            head = None
            return head
    
        del_index = size-n
        if del_index == 0:
            head = info[del_index+1][1]
        elif del_index != size-1:
            info[del_index-1][1].next = info[del_index+1][1]
        else:
            info[del_index-1][1].next = None
            
        return head