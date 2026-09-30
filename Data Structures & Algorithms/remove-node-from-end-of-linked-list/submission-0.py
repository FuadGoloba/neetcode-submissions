# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev, curr = None, head
            while curr:
                curr_nxt = curr.next
                curr.next = prev
                prev, curr = curr, curr_nxt
            return prev

        head = reverse(head)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        i = 1
        while curr.next:
            if i == n:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
            i += 1

        return reverse(dummy.next)