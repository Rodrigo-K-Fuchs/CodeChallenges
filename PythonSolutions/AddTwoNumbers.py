#──────────────────────────────────────────────k
#────────██────────██────██────────────────────a
#────────██───█████──────██────────────────────k
#────────██████──────────█████████████─────────u
#────────████████████────█████████████─────────n
#────────██─────────█────██─────────██─────────a
#────────██────────██────██─────────██─────────
#────────██────────█─────██────────██──────────
#────────██───────██─────██───────███──────────
#────────██─────██───────██─────████───────────
#────────██────██────────██───████─────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
#────────────────────────██────────────────────
#─────────────────────────██────────██─────────
#──────────────────────────██───────█──────────
#─────────────────────────────────██───────────
#────────────────────────────────██────────────
#────────████████████─────────███──────────────
#───────────────────────────██─────────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
# LEETCODE CHALLENGE Add Two Numbers
# source link Try out youself: https://leetcode.com/problems/add-two-numbers/description/
#Definition for singly-linked list.
#
#class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
       # Setting up a node and an auxiliary node to help us during the sums
        node = ListNode(0)
        auxNode = node
        # Carry to verify if we need to 'carry' a number that exceeds 10 
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            # Updating the node with the remainder of the carry if it exceeds 10
            auxNode.next = ListNode(carry%10)
            auxNode = auxNode.next
            # Updating the carry to be either 1 or 0
            carry = carry//10
            
        return node.next 
            