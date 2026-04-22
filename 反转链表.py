class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         cur = head
         pre = None
         while cur is not None:
             temp = cur.next
             cur.next = pre
             pre = cur
             cur = temp
         return pre


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head  is None or head.next  is None:
            return head

        newHead = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return newHead