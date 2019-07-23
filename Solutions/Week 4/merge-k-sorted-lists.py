# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = list(filter(lambda x: x, lists))
        if not lists:
            return None
        ls = []
        for head in lists:
            while (head):
                ls.append(head.val)
                head = head.next
        heapq.heapify(ls)
        newHead = ListNode(heapq.heappop(ls))
        curr = newHead
        while (ls):
            curr.next = ListNode(heapq.heappop(ls))
            curr = curr.next
        return newHead