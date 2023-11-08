from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        if len(list1) >= len(list2):
            for i in range(len(list1)):
                result.append(list1[i])
                result.append(list2[i])
        else:
            for i in range(len(list2)):
                result.append(list1[i])
                result.append(list2[i])
        
        return result







list1 = [1,2,4]
list2 = [1,3,4]
x = Solution().mergeTwoLists(list1, list2)
print(x)

print('---------------------------')

list1 = []
list2 = [0]
x = Solution().mergeTwoLists(list1, list2)
print(x)