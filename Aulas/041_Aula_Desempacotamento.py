"""
📦 DESEMPACOTAMENTO EM CHAMADAS DE FUNÇÕES
------------------------------------------
O operador * (asterisco) é usado para desempacotar iteráveis em chamadas de função,
distribuindo seus elementos como argumentos separados.
"""

# 🏷️ Dados de exemplo
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('Python', 'é', 'legal')
salas = [
    ['Maria', 'Helena'],   # Sala 0
    ['Elaine'],            # Sala 1
    ['Luiz', 'João', 'Eduarda']  # Sala 2
]

"""
💡 EXEMPLOS COMENTADOS:
1. Desempacotamento em variáveis:
p, b, *_, ap, u = lista  # Ignora elementos do meio com *_
print(p, u, ap)  # Maria Eduarda 3

2. Desempacotamento em print():
print('Maria', 'Helena', 1, 2, 3, 'Eduarda')  # Manual
print(*lista)  # Equivalente ao acima
print(*string)  # A B C D
print(*tupla)  # Python é legal
"""

# 🖨️ Desempacotando lista de salas com separador
print(*salas, sep='\n')
# Saída:
# ['Maria', 'Helena']
# ['Elaine']
# ['Luiz', 'João', 'Eduarda']

"""
📌 USOS COMUNS:
1. Passar elementos de lista como argumentos separados
2. Combinar iteráveis: nova_lista = [*lista1, *lista2]
3. Transposição de dados: zip(*matriz)
4. Funções que aceitam número variável de args

✨ TÉCNICAS AVANÇADAS:
"""
# Desempacotamento em dicionários (com **)
dados = {'nome': 'Maria', 'idade': 30}
print('{nome} tem {idade} anos'.format(**dados))

# Combinando operadores
valores = [*range(5), *'ABC']
print(valores)  # [0, 1, 2, 3, 4, 'A', 'B', 'C']

"""
⚠️ CUIDADOS:
1. Não use com iteráveis muito grandes (pode estourar memória)
2. A ordem do desempacotamento segue a ordem do iterável
3. Para dicionários, ** desempacota pares chave-valor
"""

"""
📚 APRENDIZADOS:
1. Sintaxe de desempacotamento com *
2. Aplicações em funções built-in
3. Combinação com outros operadores
4. Casos de uso avançados
"""