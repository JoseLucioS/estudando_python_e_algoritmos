#design de uma linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head

        for _ in range(index):
            current = current.next
        return current.value

    def addAtHead(self, val: int) -> None:
        currentNode = Node(val)
        currentNode.next = self.head
        self.head = currentNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        newNode = Node(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
            newNode.next = current.next
            current.next = newNode
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)   # linked list becomes 1->2->3
    print(linkedList.get(1))      # return 2
    linkedList.deleteAtIndex(1)   # now the linked list is 1->3
    print(linkedList.get(1))      # return 3