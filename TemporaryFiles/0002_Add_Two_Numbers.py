# number-srd = 0002
# title-srd = Add Two Numbers
# filename-srd = 0002_Add_Two_Numbers.py
# difficulty-srd = medium
# language-srd = python
# tags-srd = LINKEDLIST, MATH, RECURSION
# leetcodelink-srd = https://leetcode.com/problems/add-two-numbers/
# acceptancerate-srd = 39.8%
# notes-srd = 
# end-srd = 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ans = t = ListNode()
        carry = 0
        while(l1 or l2):
            s = 0
            if(l1):
                s += l1.val
                l1 = l1.next
            if(l2):
                s += l2.val
                l2 = l2.next
            s += carry
            t.next = ListNode(s%10)
            t = t.next
            carry = s//10
            
        if(carry):
            t.next = ListNode(carry)
            
        return ans.next