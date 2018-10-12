# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 

class Solution:
    def printNodes(self, x):
        node = x
        while(node):
            print('NODE VALUE: ', node.val)
            node = node.next
            

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        while (l1 and l2):
            if (l1.val <= l2.val):
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if (l1): p.next = l1
        elif (l2): p.next = l2
        return dummy.next

data1 = [2,4]
data2 = [2,3,4,4]
l1 = ListNode(1)
lastNode = l1

for i in data1:
    newNode = ListNode(i)
    lastNode.next = newNode
    lastNode = newNode

l2 = ListNode(1)
lastNode = l2

for i in data2:
    newNode = ListNode(i)
    lastNode.next = newNode
    lastNode = newNode

s = Solution()
newList = s.mergeTwoLists(l1, l2)
s.printNodes(newList)
