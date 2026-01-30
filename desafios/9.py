"""
Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento. O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante. O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.

Exemplo de entrada:

    participantes = { 

        "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

        "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

    }


    Nome do participante a ser removido: Carla 

Saída esperada:

    Lista atualizada de participantes: 

    Workshop 1: {'Alice', 'Bruno', 'Diego'} 

    Workshop 2: {'Fernanda', 'Gustavo', 'Helena'} 
"""


participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
}

nome = input("Nome do participante a ser removido: ")

for worlshop, nomes in participantes.items():
    nomes.discard(nome)

print("Lista atualizada de participantes: ")
for worlshop, nomes in participantes.items():
    print(f"{worlshop}: {nomes}")