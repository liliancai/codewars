# Runtime: 172 ms, faster than 28.29% of Python3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import queue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(None)
        curr = dummy
        q = queue.PriorityQueue()
        for i,node in enumerate(lists):
            if node:q.put((node.val,i,node))
        while not q.empty():
            _, i, curr.next = q.get()
            curr=curr.next
            if curr.next: q.put((curr.next.val,i, curr.next))
        return dummy.next
