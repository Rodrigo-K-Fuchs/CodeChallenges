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

# Definition for singly-linked list.
# LEETCODE CHALLENGE Add Two Numbers

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

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
            # Updating the node and the carry according to the sums 
            auxNode.next = ListNode(carry%10)
            auxNode = auxNode.next
            carry = carry//10
            
        return node.next 
            