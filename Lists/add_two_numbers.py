# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.HelperFunction(l1, l2, None, 0)
    
    def HelperFunction(self, l1, l2, l3, carry_value):
        if l1 is None and l2 is None and carry_value == 0:
            return 0
        
        p = 0
        q = 0
        next_p = None
        next_q = None
        
        if l1 is not None:
            p = l1.val
            next_p = l1.next
            
        if l2 is not None:
            q = l2.val
            next_q = l2.next
            
        total = p + q + carry_value
        new_carry_value = total // 10
        final_value = total - (new_carry_value * 10)
        next_node = ListNode(final_value)
        
        if l3 is not None:
            l3.next = next_node
            
        self.HelperFunction(next_p, next_q, next_node, new_carry_value)
        return next_node
        
