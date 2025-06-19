"""
📚 DICTIONARY E SET COMPREHENSION EM PYTHON
-------------------------------------------
Comprehensions são formas concisas de criar coleções a partir de iteráveis.
Aqui exploramos dicionários e conjuntos (sets).
"""

# 🖊️ Dicionário de exemplo
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# 1️⃣ DICTIONARY COMPREHENSION
dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'  # Filtro: exclui a chave 'categoria'
}
print("📌 Dicionário transformado:")
print(dc)  # {'nome': 'CANETA AZUL', 'preco': 2.5}

"""
💡 ANÁLISE:
- Transforma valores string em maiúsculas
- Mantém valores não-string inalterados
- Remove a entrada 'categoria'
"""

# 2️⃣ DICTIONARY COMPREHENSION com lista de tuplas
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),  # Duplicado proposital
]
dc = {chave: valor for chave, valor in lista}
print("\n📌 Dicionário de tuplas:")
print(dc)  # {'a': 'valor a', 'b': 'valor a'} (chaves duplicadas são sobrescritas)

# 3️⃣ SET COMPREHENSION
s1 = {2 ** i for i in range(10)}  # Potências de 2
print("\n📌 Conjunto de potências de 2:")
print(s1)  # {1, 2, 4, 8, 16, 32, 64, 128, 256, 512}

"""
✨ CARACTERÍSTICAS:
Dictionary Comprehension:
- Sintaxe: {chave: valor for item in iterável}
- Pode incluir condicionais para chaves e valores
- Chaves duplicadas são sobrescritas

Set Comprehension:
- Sintaxe: {expressão for item in iterável}
- Elimina automaticamente duplicatas
- Não mantém ordem (antes do Python 3.7)
"""

"""
📌 EXEMPLOS ADICIONAIS:
"""
# 🔢 Quadrados de números
quadrados = {x: x*x for x in range(5)}
print("\nQuadrados:", quadrados)

# 🔠 Filtrando letras
letras = {letra for letra in 'abracadabra' if letra not in 'abc'}
print("Letras filtradas:", letras)

"""
⚠️ CUIDADOS:
1. Não exagere na complexidade
2. Prefira funções nomeadas para lógica complexa
3. Sets não permitem elementos mutáveis
"""

"""
📚 APRENDIZADOS:
1. Sintaxe de dictionary e set comprehension
2. Como aplicar filtros e transformações
3. Diferenças entre dict e set comprehension
4. Casos de uso práticos
"""