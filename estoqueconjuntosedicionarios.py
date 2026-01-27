"""
Criando um estoque com conjuntos e dicionários
"""

estoque = {
    "frutas": {"maça", "uva"},
    "verduras": {"cenora", "alface"}
} # Dicionário com conjuntos

estoque["frutas"].add("motando") # Adicionando um item

estoque["verduras"].dicard("alface") # Removendo um item

print(estoque)