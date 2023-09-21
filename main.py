class Nodo:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Pila:
    def __init__(self, values=None):
        # Iniciamos con una lista
        self.header = values

    def peek(self):
        return self.header.value

    def push(self, value):
        new_node=Nodo(value)
        new_node.next=self.header
        self.header=new_node

    def pop(self):
        self.header=self.header.next

    def show_pila(self):
        elements=[]
        now= self.header
        while now is not None:
            elements.append(now.value)
            now=now.next
        return elements

pila1 = Pila()
pila1.push(1)
pila1.push(2)
pila1.push(3)
pila1.push(4)
pila1.pop()
pila1.push(5)

elemento = pila1.peek()
print(pila1.show_pila())
print("Ultimo elemento:", elemento)