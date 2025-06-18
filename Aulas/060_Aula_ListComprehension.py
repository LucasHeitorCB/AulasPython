"""
🚀 LIST COMPREHENSION EM PYTHON
-------------------------------
List comprehension é uma forma concisa e eficiente de criar listas a partir de iteráveis.
Sintaxe básica: [expressão for item in iterável]
"""

# 🐢 Método tradicional com loop for
lista_tradicional = []
for numero in range(10):
    lista_tradicional.append(numero)
# print(lista_tradicional)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🐍 Versão com list comprehension
lista = [numero * 2 for numero in range(10)]  # 🔄 Dobra cada número
print(lista)  # 🖨️ [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

"""
💡 VANTAGENS DA LIST COMPREHENSION:
1. Mais conciso e legível (quando simples)
2. Geralmente mais rápido que loops tradicionais
3. Pode incluir condicionais
4. Pode aninhar múltiplos loops

📌 EXEMPLOS ADICIONAIS:
"""
# 🔢 Números pares
pares = [n for n in range(20) if n % 2 == 0]
# print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 🔠 Converter para maiúsculas
nomes = ['lucas', 'heitor', 'barbosa']
maiusculas = [nome.upper() for nome in nomes]
# print(maiusculas)  # ['LUCAS', 'HEITOR', 'BARBOSA']

# 🧮 Produto cartesiano
produto = [(x, y) for x in range(3) for y in range(3)]
# print(produto)  # [(0, 0), (0, 1), (0, 2), (1, 0), ...]

"""
⚠️ CUIDADOS:
1. Não exagere na complexidade - pode reduzir legibilidade
2. Para transformações complexas, prefira loops tradicionais
3. Evite efeitos colaterais dentro da comprehension

✨ BOAS PRÁTICAS:
1. Use para transformações simples de dados
2. Mantenha em uma linha quando possível
3. Use nomes descritivos para variáveis
4. Documente compreensões complexas
"""

"""
📚 APRENDIZADOS:
1. Sintaxe básica de list comprehension
2. Quando usar vs loops tradicionais
3. Como adicionar condicionais
4. Padrões comuns de uso
"""