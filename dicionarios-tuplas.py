"""
Criando dicionários com listas de tuplas

Um dicionário pode ser criado a partir de uma lista de tuplas usando dict(). Cada tupla deve conter dois elementos: a chave e o valor.
"""

# Exemplo

listas_de_tuplas = [("nome", "Ana"), ("nota", 10.0)]

dicionario = dict(listas_de_tuplas)

print(dicionario) # Saída: {'nome': 'Ana', 'nota': 10.0}