from typing import List, Any

class Deque:
    def __init__(self):
        self.__data: List[Any] = []

    def insert_first(self, elemento: Any) -> None:
        self.__data.insert(0, elemento)
    
    def insert_last(self, elemento: Any) -> None:
        self.__data.append(elemento)
    
    def remove_first(self) -> Any:
        if self.is_empty():
            raise IndexError("Erro: Tentativa de remover de um Deque vazio.")
        return self.__data.pop(0)
    
    def remove_last(self) -> Any:
        if self.is_empty():
            raise IndexError("Erro: Tentativa de remover de um Deque vazio.")
        return self.__data.pop()
    
    def first(self) -> Any:
        if self.is_empty():
            raise IndexError("Erro: O Deque está vazio.")
        return self.__data[0]
    
    def last(self) -> Any:
        if self.is_empty():
            raise IndexError("Erro: O Deque está vazio.")
        return self.__data[-1]
    
    def is_empty(self) -> bool:
        return len(self.__data) == 0
    
    def size(self) -> int:
        return len(self.__data)

    def __str__(self) -> str:
        return str(self.__data)


if __name__ == "__main__":
    #Cria a estrutura e verifica se inicia vazia
    f_dupla = Deque()
    print(f_dupla.is_empty())
    
    #Inserção de elementos nas duas extremidades (Início e Fim)
    f_dupla.insert_first("Item B")
    f_dupla.insert_first("Item A")
    f_dupla.insert_last("Item C")
    f_dupla.insert_last("Item D")
    
    #Exibe o estado atual da estrutura após inserções
    print(f_dupla)
    
    #Consulta (espia) os elementos das pontas sem remover
    print(f_dupla.first())
    print(f_dupla.last())
    
    #Remove elementos de ambas as extremidades e mostra o valor removido
    print(f_dupla.remove_first())
    print(f_dupla.remove_last())
    
    #Verifica a quantidade de elementos restantes
    print(f_dupla.size())
    
    #Esvazia completamente o Deque para preparar o teste de erro
    f_dupla.remove_first()
    f_dupla.remove_first()
    
    #Bloco de tratamento para validar a tentativa de remoção em Deque vazio
    try:
        f_dupla.remove_first()
    except IndexError as erro:
        print(erro)