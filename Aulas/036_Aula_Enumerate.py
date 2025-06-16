"""
🔢 ENUMERATE EM PYTHON - ÍNDICES EM ITERÁVEIS
--------------------------------------------
A função enumerate() adiciona um contador a um iterável e retorna um objeto enumerado.
É útil quando você precisa tanto do valor quanto do índice durante a iteração.

Retorna: (índice, valor) para cada item
"""

# 📍 Lista de nomes (iterável)
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')  # Adiciona novo nome

# 🔄 Forma mais comum de usar enumerate
for indice, nome in enumerate(lista):
    # 🖨️ Imprime índice, nome e valor através da lista
    print(indice, nome, lista[indice])
    # Saída:
    # 0 Maria Maria
    # 1 Helena Helena
    # 2 Luiz Luiz
    # 3 João João

"""
💡 VERSÕES ALTERNATIVAS (COMENTADAS):
"""
# # 1️⃣ Acessando a tupla diretamente
# for item in enumerate(lista):
#     indice, nome = item  # Desempacota a tupla
#     print(indice, nome)

# # 2️⃣ Iterando dentro da tupla
# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

"""
📌 PARÂMETROS IMPORTANTES:
enumerate(iterable, start=0)
- start: define o valor inicial do contador (padrão 0)

✨ EXEMPLOS ÚTEIS:
"""
# Enumerando a partir de 1
for i, nome in enumerate(lista, start=1):
    print(f'Posição {i}: {nome}')

# Convertendo para lista de tuplas
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)  # [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]

"""
🚀 CASOS DE USO COMUNS:
1. Acessar índice e valor simultaneamente
2. Criar dicionários a partir de listas
3. Processar arquivos mantendo contagem de linhas
4. Implementar sistemas de ranking/posicionamento

🔍 DICA AVANÇADA:
Você pode usar enumerate com qualquer iterável:
- Strings, dicionários, arquivos, geradores, etc.
"""

"""
📚 APRENDIZADOS:
1. Como acessar índices durante iteração
2. Formas alternativas de usar enumerate
3. Controle do valor inicial
4. Aplicações práticas
"""