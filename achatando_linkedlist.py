#Dada uma lista duplamente ligada em que cada nó pode ter ou não um nó child que aponta para uma
#sub-lista, achate a lista para que todos os nós apareçam em uma única lista duplamente ligada,
#transformando a lista que antes estava em multicamadas em uma lista de camada única.
class ListNode:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

#forma iterativa usando pilha
def flatten(self, head):
        if not head:
            return None
        
        stack = [head]
        prev = None
        
        while stack:
            curr = stack.pop()
            
            if prev:
                prev.next = curr
                curr.prev = prev
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            prev = curr
        
        return head