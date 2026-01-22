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