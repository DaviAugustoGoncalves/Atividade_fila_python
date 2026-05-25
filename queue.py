class Queue:
    """Fila simples (FIFO)"""

    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        # adiciona no final da fila
        if self.is_full():
            raise OverflowError("Fila cheia, não dá pra adicionar mais")
        self.items.append(item)

    def dequeue(self):
        # remove o primeiro da fila
        if self.is_empty():
            raise IndexError("Fila vazia, nada pra remover")
        return self.items.pop(0)

    def peek(self):
        # olha o primeiro sem remover
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.max_size is None:
            return False
        return len(self.items) >= self.max_size

    def size(self):
        return len(self.items)

    def clear(self):
        # limpa a fila inteira
        self.items = []

    def __str__(self):
        return str(self.items)


# testes simples
if __name__ == "__main__":

    print("começando testes...")

    fila = Queue()

    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)

    assert fila.size() == 3
    print("size ok")

    assert fila.peek() == 10
    print("peek ok")

    assert fila.dequeue() == 10
    assert fila.dequeue() == 20
    print("dequeue ok")

    assert not fila.is_empty()
    print("ainda tem item")

    fila.dequeue()
    assert fila.is_empty()
    print("agora tá vazia")

    try:
        fila.dequeue()
    except IndexError:
        print("erro dequeue ok")

    try:
        fila.peek()
    except IndexError:
        print("erro peek ok")

    fila2 = Queue(max_size=2)
    fila2.enqueue(1)
    fila2.enqueue(2)

    assert fila2.is_full()
    print("fila cheia ok")

    try:
        fila2.enqueue(3)
    except OverflowError:
        print("overflow ok")

    fila2.clear()
    assert fila2.is_empty()
    print("clear ok")

    print("fim dos testes")
