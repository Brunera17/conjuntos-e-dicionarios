"""
Métodos de manipulação

Existem diversos métodos de operações entre conjuntos.
"""

# Considere:
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)    # União de dois conjuntos. ex: union(set2) ou (|)
a|b

a.intersection(b)    # Interseção de dois conjuntos. ex: intersection(set2) ou (&)
a&b

a.difference(b)    # Diferença entre dois conjuntos, considerando elementos exclusivos do primeiro conjunto.
a-b                # ex: difference(set2) ou (-)

a.symmetric_difference(b)    # Diferença entre dois conjuntos, considerando elementos exclusivos de ambos conjuntos.
a^b                          # symmetric_difference(set2) ou (^)

""" 
Podemos analisar a relação entre conjuntos e suas características utilizando alguns métodos e criar cópias de conjuntos.
"""

# Considere:
a = {1, 2}
b = {1, 2, 3, 4}

a.issubset(b)    # Verifica se um conjunto é subconjunto de outro.
a<=b             # ex: issubset(set2) ou (<=)

a.issuperset(b)    # Verifica se um conjunto é superconjunto de outro.
a>=b               # ex: issuperset(set2) ou (>=)

c = {5, 6, 7}    # Verfica se ps conjuntos não tem elementos em comum
a.isdisjoint(c)  # ex: isdisjoin(set2)

len(a)    # Verifica o número de elementos de um conjunto. ex: len(conjunto)

copia = a.copy()    # Retorna uma cópia do conjunto.
print(copia)        # ex: copy()