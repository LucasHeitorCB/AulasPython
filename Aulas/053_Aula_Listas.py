"""
📌 LISTAS EM PYTHON (TIPO list)
--------------------------------
Listas são estruturas mutáveis que armazenam coleções de itens.
Principais características:
- Mutável: pode ser alterada após criação
- Indexada: acessa elementos por índices (começando em 0)
- Heterogênea: pode armazenar diferentes tipos de dados
- Ordenada: mantém a ordem de inserção
"""

# 🏷️ Criando uma lista inicial
lista = [10, 20, 30, 40]  # Índices: 0:10, 1:20, 2:30, 3:40

# 🔄 Operações CRUD (Create, Read, Update, Delete) comentadas:
# lista[2] = 300    # ✏️ Update: altera o valor no índice 2 para 300
# del lista[2]      # 🗑️ Delete: remove o item no índice 2
# print(lista[2])   # 👀 Read: imprime o valor no índice 2

# ➕ Adicionando itens
lista.append(50)  # 📥 Adiciona 50 ao FINAL da lista → [10, 20, 30, 40, 50]

# 🗑️ Removendo itens
lista.pop()       # 📤 Remove o ÚLTIMO item → [10, 20, 30, 40]

# ➕ Adicionando mais itens
lista.append(60)  # → [10, 20, 30, 40, 60]
lista.append(70)  # → [10, 20, 30, 40, 60, 70]

# 🗑️ Removendo item específico
ultimo_valor = lista.pop(3)  # 📦 Remove e retorna o item no índice 3 (40)
print(lista, 'Removido,', ultimo_valor)  # 🖨️ [10, 20, 30, 60, 70] Removido, 40

"""
💡 MÉTODOS ÚTEIS DE LISTAS:
1. append(valor) - adiciona ao final
2. insert(índice, valor) - insere em posição específica
3. pop(índice) - remove e retorna item (ou último se omitido)
4. remove(valor) - remove primeira ocorrência do valor
5. clear() - esvazia a lista
6. extend(iterável) - adiciona vários itens

📌 EXEMPLOS ADICIONAIS:
- lista + [1, 2] → concatena listas
- lista *= 2 → repete a lista
- lista.copy() → cópia superficial
- lista.reverse() → inverte a ordem
"""

"""
⚠️ CUIDADOS IMPORTANTES:
1. Índices fora do range causam IndexError
2. pop() em lista vazia causa IndexError
3. remove() para valor inexistente causa ValueError
4. Atribuição direta cria referência, não cópia
"""

"""
✨ BOAS PRÁTICAS:
1. Use list comprehension para transformações
2. Prefira métodos nativos a loops quando possível
3. Documente a estrutura esperada da lista
4. Para grandes coleções, considere generators
"""