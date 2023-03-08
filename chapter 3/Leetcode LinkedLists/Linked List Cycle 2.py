# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        explored = set() #dict would be slower but slightly memory efficient, wow

        while current:
            if current in explored:
                return current
            else:
                explored.add(current)
                current = current.next

    # wow this is shit and long
    #
    # def detectCycle(self, head):
    #     if self.hasCycle(head):
    #         explored = []
    #         current = head
    #         while current not in explored:
    #             explored.append(current)
    #             current = current.next
    #         return current
    #     else:
    #         return None
    #
    # def hasCycle(self, head):
    #     if head is None or head.next is None:
    #         return False
    #     slow = head
    #     fast = head.next
    #     while slow != fast:
    #         if fast.next is None or fast.next.next is None:
    #             return False
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow is None or fast is None:
    #             return False
    #     return True

