'''
Solution1: 
Split linked list into left, middle, right. Reverse middle, then combine left and right.
Cons: Need to be careful about edge cases
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = head
        dummy = ListNode(0, head)
        head = dummy
        
        endHead = None
        tempEndHead = None
        if(right>=1):
            tempEndHead = head
            for _ in range(right+1):
                tempEndHead = tempEndHead.next
            if(tempEndHead):
                endHead = tempEndHead
        

        midHead = None
        midTail = None
        tempMidHead = head
        tempMidTail = head
        for _ in range(left):
            tempMidHead = tempMidHead.next
        for _ in range(right):
            tempMidTail = tempMidTail.next
        midHead = tempMidHead
        midTail = tempMidTail
        tempMidTail.next = None

        startHead = None
        startTail = None
        tempStartHead = None
        tempStartTail = None
        if(left>=1):
            startHead = None
            startTail = None
            tempStartHead = head
            tempStartTail = head
            for _ in range(left-1):
                tempStartTail = tempStartTail.next
            startTail = tempStartTail
            startTail.next = None

        
        prevNode = None
        if(midHead):
            midTail = midHead
        while midHead:
            nextNode = midHead.next
            midHead.next = prevNode
            prevNode = midHead
            midHead = nextNode
    
        print(startTail)
        print(prevNode)
        print(midTail)
        print(endHead)
        
        if(startTail.val==0):
            dummy.next = prevNode
            if midTail:
                midTail.next = endHead
            return dummy.next
        else:
            startTail.next = prevNode
            if midTail:
                midTail.next = endHead
            return ans
        
'''
Solution2: 
Added dummy data to prevent edge cases

Traverse linked list and reverse the list as we go. Need to keep data 
about starting point of center (prevL) and ending point of center (prev)
to connect the reversed nodes to the original list.
'''

class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevL, curr = dummy, head
        for _ in range(left-1):
            prevL = curr
            curr = curr.next
         # traverse until we reach center for reversing
         # keep prevL to later connect the start and end of reversed list
        
        prev = None
        for _ in range(right - left + 1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        prevL.next.next = curr
        prevL.next = prev
        return dummy.next