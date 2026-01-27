"""
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

Quais itens apareceram nas duas listas

Quais foram exclusivos de Laura

Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

Exemplo de entrada:

    Lista de Laura: leite, pão, café, açúcar 

    Lista de Ana: pão, café, biscoito, chocolate 

Saída esperada:

    Itens em ambas as listas: pão, café 

    Itens exclusivos de Laura: leite, açúcar 

    Itens exclusivos de Ana: biscoito, chocolate 
"""
laura = set(input("Lista de Laura: ").lower().split(', '))
ana = set(input("Lista de Ana: ").lower().split(', '))

comuns = laura&ana
exclusivos_laura = laura-ana
exclusivos_ana = ana-laura

print(f"Itens em ambas as listas: {', '.join(comuns)}")
print(f"Itens exclusivos de Laura: {', '.join(exclusivos_laura)}")
print(f"Itens excluisvos de Ana: {', '.join(exclusivos_ana)}")
