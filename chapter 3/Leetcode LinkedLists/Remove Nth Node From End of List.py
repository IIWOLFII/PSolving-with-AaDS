# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #could be done while just retaining space of n inbetween slow and fast i should try that soon
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous = None
        current = head

        size = 0
        while current:
            size += 1
            current = current.next

        size = size - n  # we stop when current in size - n spot which is one more than required index
        current = head

        while size != 0 and current:
            previous = current
            current = current.next
            size -= 1

        if previous is None:
            head = current.next
            return head

        if current is None:
            previous.next = None
            return head

        previous.next = current.next
        return head






