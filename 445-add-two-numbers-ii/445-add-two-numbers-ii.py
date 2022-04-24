# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = []
        st2 = []
        
        head = None
        
        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next
        carry = 0 
        while st1 or st2:
            num1 = st1.pop() if st1 else 0
            num2 = st2.pop() if st2 else 0
            
            carry, num = divmod(num1 + num2 + carry, 10)
            
            node = ListNode(num)
            if not head:
                head = node
            else:
                temp = head
                head = node
                node.next = temp
        if carry:
            node = ListNode(carry)
            temp = head
            head = node
            node.next = temp
        return head
            
            