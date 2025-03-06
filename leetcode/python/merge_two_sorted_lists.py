from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        
        return dummy.next


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    current = merged_list
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

    list1 = None
    list2 = None
    merged_list = solution.mergeTwoLists(list1, list2)
    print("Lista vazia" if not merged_list else merged_list.val)

    list1 = None
    list2 = ListNode(0)
    merged_list = solution.mergeTwoLists(list1, list2)

    current = merged_list
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next
