# Atividade_fila_python

Esse projeto foi feito para uma atividade de estrutura de dados. A ideia foi implementar uma fila simples em Python usando lista, sem usar deque.

A fila funciona no modelo FIFO, ou seja, o primeiro elemento que entra é o primeiro a sair.

A classe Queue tem métodos básicos como adicionar item no final (enqueue), remover o primeiro item (dequeue), ver o primeiro sem remover (peek), verificar se está vazia ou cheia, ver o tamanho e também limpar a fila inteira. Se tentar remover de uma fila vazia ou adicionar em uma fila cheia (quando tem limite), o código gera erro.
Os testes já estão no próprio arquivo e rodam automaticamente quando executa o programa. Eles testam situações normais e alguns erros básicos como fila vazia e fila cheia.
