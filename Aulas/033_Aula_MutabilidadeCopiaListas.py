"""
🔄 ENTENDENDO MUTABILIDADE E CÓPIA DE LISTAS EM PYTHON
-----------------------------------------------------
Em Python, dados mutáveis (como listas) têm comportamento diferente na atribuição:
- Atribuição direta (=) cria referência ao mesmo objeto
- .copy() cria uma nova lista independente
"""

# 🏷️ Lista original (mutável)
lista_a = ['Luiz', 'Maria', 1, True, 1.2]

# 📋 Criando uma cópia real da lista
lista_b = lista_a.copy()  # 🆕 Versão independente da lista

# ✏️ Modificando apenas a lista original
lista_a[0] = 'Qualquer coisa'  # 🔄 Altera apenas lista_a

# 🖨️ Resultados (lista_a modificada, lista_b intacta)
print(lista_a)  # ['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_b)  # ['Luiz', 'Maria', 1, True, 1.2] (original preservada)

"""
💡 POR QUE ISSO É IMPORTANTE?
1. Com dados mutáveis (listas, dicionários, sets):
   - Atribuição direta: lista_b = lista_a → ambas apontam para mesma lista
   - Modificação em uma afeta a "outra" (que na verdade é a mesma)

2. Com dados imutáveis (strings, números, tuplas):
   - Atribuição sempre cria cópia automática
   - Modificações não afetam o original

🔍 DEMONSTRAÇÃO DO PROBLEMA (se não usar .copy()):
lista_c = lista_a  # ❌ Ambas apontam para mesma lista
lista_c[0] = 'Oops'  # ✏️ Modifica ambas!
print(lista_a)  # ['Oops', ...] - indesejado!

📌 OUTRAS FORMAS DE COPIAR LISTAS:
1. Slice completo: lista_b = lista_a[:]
2. Constructor: lista_b = list(lista_a)
3. copy.deepcopy() para listas aninhadas

✨ BOAS PRÁTICAS:
- Sempre use .copy() quando quiser uma nova lista independente
- Para listas complexas (com outras listas dentro), use copy.deepcopy()
- Documente claramente quando compartilhamento é intencional
"""

"""
📚 APRENDIZADOS:
1. Diferença entre mutáveis e imutáveis na atribuição
2. Como criar cópias reais de listas
3. Riscos de compartilhamento não intencional
4. Alternativas para copiar listas
"""