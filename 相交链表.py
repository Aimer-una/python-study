class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        q = headA
        p = headB
        while q not in p:
            q = q.next if q else headB
            p = p.next if p else headA
        return p