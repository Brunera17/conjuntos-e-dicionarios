"""
Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

Exemplo de entrada:

    > CASO 01: 

    Permissões principais: leitura, escrita, execução, compartilhamento 

    Permissões solicitadas: leitura, escrita 

    > CASO 02: 

    Permissões principais: leitura, escrita, execução, compartilhamento 

    Permissões solicitadas: leitura, exclusão 

Saída esperada:

    > CASO 01: 

    As permissões solicitadas fazem parte das permissões principais. 

    > CASO 02: 

    As permissões solicitadas não fazem parte das permissões principais.
"""

lista1 = set(input("Permissões principais: ").split(', '))
lista2 = set(input("Permissões solicitadas: ").split(', '))

if lista1>=lista2:
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
    print("As permissões solicitadas não fazem parte das permissões principais.")

# Correção

permissoes_principais = set(input("Permissões principais: ").strip().lower().split(',')) 

permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(',')) 

for i in range(len(permissoes_principais)):  

    permissoes_principais[i] = permissoes_principais[i].strip() 

for i in range(len(permissoes_solicitadas)):  

    permissoes_solicitadas[i] = permissoes_solicitadas[i].strip() 

eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais) 

if eh_subconjunto:  

    print("As permissões solicitadas fazem parte das permissões principais.")  

else:  

    print("As permissões solicitadas não fazem parte das permissões principais.") 

""" 
Quando pedimos para o usuário digitar as permissões, ele pode inserir os valores de forma inconsistente, com espaços extras, letras maiúsculas e minúsculas misturadas, ou até mesmo separadores errados. Se não tratarmos a entrada corretamente, comparações podem falhar.

Para garantir que os dados estejam sempre no mesmo formato, utilizamos três funções principais:

    strip(): Remove espaços extras e cada permissão pode ter espaços antes ou depois da vírgula.

    lower(): Converte para letras minúsculas, assim, se o usuário digitar "EXECUÇÃO" e compararmos com "execução", a verificação pode falhar, pois Python diferencia maiúsculas e minúsculas.

    split(','): Divide a string em uma lista de elementos e transforma a entrada do usuário em uma lista separada por vírgula, permitindo criar um conjunto posteriormente.

"""