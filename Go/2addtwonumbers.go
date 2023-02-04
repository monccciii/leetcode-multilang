/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/*
How this works:
create another linked list (ListNode) named dummyHead
create a pointer to dummyhead called curr
create a variable named carry for addition carryover
create a while loop that checks whether l1 l2 haven't been fully iterated through and lets carry be added regardless (edge case)
initialize pointers to l1,l2's
calculate the sum of each column in the addition, l1Val + l2Val + carry
get carry by dividing the sum by 10
get the actual value of the sum by taking the leftover numbers from the carry
update curr.next as newNode, and set curr = to newNode so next iteration can start from there
update pointers to l1 and l2 as their next value for iteration

Difference between this and python:
Virtually none, only difference is that you have to use & to get addresses
also, you could remove newNode and just put & + ListNode{...} to simplify code
*/
package main

import (
	"fmt"
)

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummyHead := ListNode{Val: 0}
    curr := &dummyHead
    carry := 0
    fmt.Println(dummyHead, curr, carry)
    for l1 != nil || l2 != nil || carry != 0 {
        l1Val := 0
        if l1 != nil {
            l1Val = l1.Val
            }
        l2Val := 0
        if l2 != nil {
            l2Val = l2.Val
            }
        columnSum := l1Val + l2Val + carry
        carry = columnSum / 10
        curr.Next = &ListNode{Val: columnSum % 10}
        curr = curr.Next
        if l1 != nil {
            l1 = l1.Next
        } else {
            l1 = nil
        }
        if l2 != nil {
            l2 = l2.Next
        } else {
            l2 = nil
        }
    }
    return dummyHead.Next
}