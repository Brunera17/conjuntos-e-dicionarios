"""
Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos. Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

Exemplo de entrada:

    Texto 1: O sol brilha forte no céu azul 

    Texto 2: O céu azul anuncia um dia de sol intenso 

Saída esperada:


    Palavras em comum: {'o', 'azul', 'sol', 'céu'} 
"""

texto1 = set(input("Texto 1: ").lower().split())
texto2 = set(input("Texto 2: ").lower().split())
comum = set()
if not texto1.isdisjoint(texto2):
    for palavra in texto1:
        if palavra in texto2:
            comum.add(palavra)
print(f"Palavras em comum: {', '.join(comum)}")
# Ou

comuns = texto1&texto2    # Pode ser usado 'texto1.intersection(texto2)'
print(f"Palavras em comum: {comuns}")