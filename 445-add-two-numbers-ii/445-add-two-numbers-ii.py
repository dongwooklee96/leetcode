# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = []
        st2 = []
        
        l1_curr = l1
        l2_curr = l2
        
        head = None
        
        while l1_curr != None:
            st1.append(l1_curr.val)
            l1_curr = l1_curr.next

        while l2_curr != None:
            st2.append(l2_curr.val)
            l2_curr = l2_curr.next
        
        carry = 0
        while st1 or st2:
            num1 = st1.pop() if st1 else 0
            num2 = st2.pop() if st2 else 0
            
            carry, num = divmod(num1 + num2 + carry, 10)
            
            node = ListNode(num)
            if head == None:
                head = node
            else:
                temp = head
                head = node
                node.next = temp
        if carry != 0:
            node = ListNode(carry)
            temp = head
            head = node
            node.next = temp
        return head    
            