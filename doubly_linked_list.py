#implementação de uma lista duplamente encadeada em python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def addAtHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = ListNode(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        
        new_node = ListNode(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            if current.next:
                current.next.prev = current
        self.size -= 1

if __name__ == "__main__":
    dll = doubly_linked_list()
    dll.addAtHead(1)
    dll.addAtTail(3)
    dll.addAtIndex(1, 2)   # lista agora é 1->2->3
    print(dll.get(1))      # retorna 2
    dll.deleteAtIndex(1)   # agora a lista é 1->3
    print(dll.get(1))      # retorna 3