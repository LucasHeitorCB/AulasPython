"""
📌 TUPLAS EM PYTHON - LISTAS IMUTÁVEIS
-------------------------------------
Tuplas são sequências imutáveis, frequentemente usadas para dados que não devem ser alterados.
Diferenças-chave para listas:
- Sintaxe: parenteses () em vez de colchetes []
- Imutáveis (não podem ser modificadas após criação)
- Mais eficientes em memória que listas
"""

# 📍 Criando uma tupla
nomes = ('Maria', 'Helena', 'Luiz')  # 👈 Sintaxe com parênteses

# Conversões (comentadas para referência):
# nomes = tuple(nomes)  # Converte para tupla (redundante aqui)
# nomes = list(nomes)   # Converte para lista (cria nova lista mutável)

# Acessando elementos:
print(nomes[-1])  # 🖨️ 'Luiz' (último elemento) 
print(nomes)      # 🖨️ Tupla completa: ('Maria', 'Helena', 'Luiz')

"""
💡 QUANDO USAR TUPLAS?
1. Para dados constantes (ex: dias da semana, meses)
2. Quando você precisa garantir que os dados não serão alterados
3. Como chaves de dicionários (listas não podem ser chaves)
4. Para retornar múltiplos valores de funções

🔍 MÉTODOS DISPONÍVEIS:
.count(x) → conta ocorrências de x
.index(x) → retorna índice da primeira ocorrência de x

⚠️ CUIDADO:
Apesar da imutabilidade, se a tupla contiver objetos mutáveis 
(como listas), esses objetos internos podem ser alterados.
"""

"""
📚 EXEMPLOS ADICIONAIS:
"""
# Tupla com um único elemento (precisa de vírgula)
singular = ('item',)  # 👈 Note a vírgula

# Tupla sem parênteses (packing)
coordenadas = 4.21, 9.29  # 👈 Automaticamente empacotada como tupla

# Desempacotamento de tupla
x, y = coordenadas  # x=4.21, y=9.29

"""
✨ BOAS PRÁTICAS:
1. Use tuplas para grupos de dados relacionados
2. Prefira para pequenas coleções de itens
3. Nomeie tuplas para melhor legibilidade (ex: from collections import namedtuple)
"""

"""
🆚 COMPARAÇÃO COM LISTAS:
- Tuplas: mais rápidas, menos memória, imutáveis
- Listas: mutáveis, mais métodos disponíveis
"""