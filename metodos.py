"""
Conjuntos possuem diversos métodos para adicionar e remover elementos.
"""

#Considere
conjunto = {1, 2, 3}

conjunto.add(4)            # Adiciona um único elemento. ex: add(elemento)
conjunto.update([5,6,7])   # Adiciona vários elementos de uma vez. ex: update(iteráveis)
conjunto.remove(2)         # Remove um item. Se o elemento não existir, gera um KeyError. ex: remove(elemento)
conjunto.dicard(2)         # Remove um item. Se o elemento não existir, não gera erro. ex: discard(elemento)
conjunto.pop()             # Remove e retorna um elemento. ex: pop()
conjunto.clear()           # Remove todos os elementos do conjunto. ex: clear()