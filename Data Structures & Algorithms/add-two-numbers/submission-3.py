# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy 

        # initialize carry to be 0 
        carry = 0 
        # keep iterating if there is still num in either l1 or l2 
        # if carry is not zero, also need to consider
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            # new digit
            val = v1 + v2 + carry 
            carry = val // 10 
            val = val % 10 
            # point cur to new node with val of new digit 
            cur.next = ListNode(val)

            # iterate pointer
            cur = cur.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        
        return dummy.next 