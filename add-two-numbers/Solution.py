// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur=l1
        l1.val = l1.val+l2.val #update the linked list l1 and update it's value, in the end we return l1 as result head node
        if(l1.val>9):
            l1.val=l1.val%10
            carry=1
        else:
            carry=0        
        while((l1.next!= None) and (l2.next!= None)):
            l1=l1.next
            l2=l2.next
            if(carry==1):
                l1.val= l1.val+l2.val+carry
            else:
                l1.val= l1.val+l2.val
            if(l1.val>9):
                l1.val=l1.val%10
                carry=1
            else:
                carry=0
        while(l1.next!=None):
            l1=l1.next
            l1.val=l1.val+carry
            if(l1.val>9):
                l1.val=l1.val%10
                carry=1
            else:
                carry=0
        if(l1.next==None and l2.next!=None):
            l1.next=l2.next
        while(l1.next!=None):
            l1=l1.next
            l1.val=l1.val+carry
            if(l1.val>9):
                l1.val=l1.val%10
                carry=1
            else:
                carry=0
        if(carry==1):
            l1.next=ListNode(1)
            # l2.next=ListNode(1)
        return cur