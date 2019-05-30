# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        root = result = ListNode(0)
        summary = 0 
        while (l1 or l2 or summary):
            if l1:
                summary += l1.val
                l1 = l1.next
            if l2:
                summary += l2.val
                l2 = l2.next
            result.next = ListNode( summary % 10)
            result = result.next
            summary //= 10
        return root.next
       
    
------------------------java 2ms--------------------
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode p3 = head, p1=l1,p2=l2;
        int digit=0,v1,v2;
        while(p1!=null||p2!=null||digit!=0){
            if(p1!=null) v1=p1.val; else v1=0;
            if(p2!=null) v2=p2.val; else v2=0;
            
            int sum = v1+v2+digit;
            p3.next =new ListNode(sum%10);
            p3=p3.next;
            digit=sum/10;
            if(p1!=null)p1=p1.next;
            if(p2!=null)p2=p2.next;
           
        }
        return head.next;
    }
}
