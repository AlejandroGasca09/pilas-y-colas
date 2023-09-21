class Nodo:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Cola:
    def __init__(self):
        self.header = None
        self.queue = None

    def enqueue(self, value):
        new_nodo = Nodo(value)
        if self.header is None:
            self.header = new_nodo
            self.queue = new_nodo
        else:
            self.queue.next = new_nodo
            self.queue = new_nodo

    def dequeue(self):
        if self.header is not None:
            self.header = self.header.next
        else:
            print("La cola está vacía")

    def peek(self):
        if self.queue is not None:
            return self.queue.value
        else:
            print("La cola está vacía")

    def show_cola(self):
        current=self.header
        while current:
            print(current.value)
            current=current.next
        return current

Cola1= Cola()
Cola1.enqueue(1)
Cola1.enqueue(2)
Cola1.enqueue(3)
print(Cola1.peek())
Cola1.show_cola()