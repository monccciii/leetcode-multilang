# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# How this works:
# create another linked list (ListNode) named dummyHead
# create a pointer to dummyhead called curr
# create a variable named carry for addition carryover
# create a while loop that checks whether l1 l2 haven't been fully iterated through and lets carry be added regardless (edge case)
# initialize pointers to l1,l2's values
# calculate the sum of each column in the addition, l1Val + l2Val + carry 
# get carry by dividing the sum by 10
# get the actual value of the sum by taking the leftover numbers from the carry 
# update curr.next as newNode, and set curr = to newNode so next iteration can start from there
# update pointers to l1 and l2 as their next value for iteration

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        print(dummyHead.next)
        return dummyHead.next