from typing import Any, List

class Stack:

    def __init__(self) -> None:
        self.__data: List[Any] = []

    def push(self, item: Any) -> None:
        self.__data.append(item)

    def __repr__(self) -> str:
        return str(self.__data)
    
    def pop(self) -> Any:
        if not self.__data:
            return None
        return self.__data.pop()
    
    def is_empty(self) -> bool:
        return len(self.__data) == 0
    
    def size(self) -> int:
        return len(self.__data)
    
    def peek(self) -> Any:
        if not self.__data:
            return None
        return self.__data[-1]
    
    def invert_list(self) -> list:
        pilha_auxiliar = Stack()
        lista_invertida = []

        while not self.is_empty():
            item = self.pop()
            lista_invertida.append(item)
            pilha_auxiliar.push(item)

        while not pilha_auxiliar.is_empty():
            item = pilha_auxiliar.pop()
            self.push(item)
