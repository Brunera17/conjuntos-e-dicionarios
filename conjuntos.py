"""
Um conjunto é uma coleção não ordenada de elementos únicos. Em Python, conjuntos são implementados usando a classe `set`. Eles suportam operações matemáticas como união, interseção e diferença.
"""

"""
Chaves {} podem ser usadas para criar conjuntos diretamente, quando contiverem elementos. Use uma lista de elementos separados por vírgulas entre chaves. 
"""
conjunto1 = {'a', 'b', 'c'}

""" 
A função set() pode ser usada para criar conjuntos, especialmente quando precisamos inicializar um conjunto vazio.
"""
conjunto2 = set([3, 4, 5, 6])

""" 
Conjunto Vazio é uma coleção que não tem elementos
"""

tipo = type({})
print(tipo) # Saída: <class 'dict'> - chaves vazias ciram outra estrutura, não um conjunto

conjunto_vazio = set() # Para conjuntos vazios, use set() sem argumentos.