#Somando dois números representados por listas encadeadas
class ListNode():
     def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0 #armazena o valor de transporte para cada soma de dígitos (vai um)
        
        while l1 or l2 or carry:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0
            
            total = value_1 + value_2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next