# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Runtime 44ms, 60%
# Got the idea from Hint
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # two pointers, behand-n-ahead, once the ahead hit end
        # the next one of behand is the targe
        ahead = behand = self
        self.next = head
        while(ahead.next):
            ahead = ahead.next
            if n:
                n -=1
            else:
                behand = behand.next
        behand.next = behand.next.next
        return self.next
