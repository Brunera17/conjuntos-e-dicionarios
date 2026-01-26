"""
Dicionários são estruturas de dados que armazenam pares chave-valor, permitindo acesso rápido aos valores por meio das chaves, Eles servem para organizar dados de forma estruturada.
Usamos chaves {} para criar dicionários diretamente, inserindo pares chave-valor separados por vírgulas, Cada par deve ter a chave e o valor separados por dois pontos (:).
"""

# Exemplo
dic1 = {"Nome": "Ana", "Nota": 10.0}

""" 
A função dict() pode ser usada para criar dicionários, passando pares chave-valor como argumentos nomeados ou utilizando uma lista de tuplas.
"""
# Exemplo
dic2 = dict(nome="Eva", nota=9.4)

""" 
Dicionários vazios

Um dicionário vazio é um dicionário sem nenhum elemento.
"""

dicionario = {}
dicionario = dict()

""" 
Um dicionário vazio pode ser criado usando {} ou dict(). Ele não contém nenhum par chave-valor inicialmente, mas pode ser preenchido conforme necessário.
"""
""" 
Tipos permitidos para chaves

As chaves de um dicionário devem ser imutáveis. Isso significa que podem ser:
    Strings -> "nome"
    Números (inteiros ou ponto flutuante) -> 1 ou 3.14
    Tuplas (desde que todos os elementos também sejam imutáveis) -> (1, 2, 3)
Mas não podem ser:
    Listas e dicionários, por serem mutáveis.
"""

# Exemplo

dicionario_valido = {1: "um", "dois": 2, (3, 4): "par"}

dicionario_invalido = {[1, 2]: "lista"} # Saída: TypeError: unhashable type: 'list'

""" 
Tipos permitidos para valores

Os valores de um dicionário podem ser qualquer tipo de dado, incluindo:
    Strings -> "nome"
    Números (inteiros ou pontos flutuante) -> 1 ou 3.14
    Tuplas -> (1,2,3)
    Listas e dicionários -> [1,2,3] ou {"chave": "valor"}
    Objetos personalizados -> Pessoa("Alice")
"""

# Exemplo
dicionario = {
    "nome": "João",
    "idade": 25,
    "notas": [10.0, 6.3, 7.5],
    "endereco": {
        "cidade": "São Paulo",
        "bairro": "Centro"
    }
}

dic = {"nome": "Ana", "nota": 10.0}

dic["nome"]     # Acessar um valor por uma chave.
                # nome_dicionario[chave] 

dic["nota"]=9.2     # Atribui um valor de uma chave.
                    # nome_dicionario[chave] = valor

del dic["nome"]     # Remove um item específico
                    # del nome_dicionario[chave]

print("nome" in dic)    # Verifica se uma chave está presente no dicionário. Ele retorna True se a chave estiver e False caso contrário.
print("idade" in dic)

print("idade" not in dic) # Verifica se uma chave não está presente em um dicionário. ELe retorna True se a chave não estiver e False caso contrário.


""" 
Dicionários possuem diversos métodos para acessar seus dados e verificar seu tamanho.
"""

# Considere
dicionario = {"nome": "João", "idade": 28}

dicionario.key()    # Retorna as chaves do dicionário.

dicionario.values()    # Retorna os valores do dicionário.

dicionario.items()    # Retorna pares (chave, valor) como tuplas.

len(dicionario)    # Contar quantos pares (chave, valor) o dicionário possui.

