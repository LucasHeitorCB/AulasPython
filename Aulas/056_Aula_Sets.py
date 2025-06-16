"""
📊 CONJUNTOS (SETS) EM PYTHON
-----------------------------
Sets são coleções não ordenadas de elementos únicos, inspirados na teoria matemática de conjuntos.
São ideais para operações de união, interseção e diferença.
"""

# 🆕 Criando conjuntos
s1 = set()  # Conjunto vazio
s1 = {'Lucas', 1, 2, 3}  # Conjunto com valores

# 🔍 Características dos sets:
# - Não permitem valores mutáveis como elementos
# - Eliminam automaticamente duplicatas
# - Não mantêm ordem dos elementos
# - Não possuem índices
# - São iteráveis (podem ser usados em loops)

# ✨ Métodos úteis:
s1.add('Heitor')  # ➕ Adiciona um elemento
s1.update([4, 5]) # 🔄 Adiciona vários elementos
s1.discard(2)     # 🗑️ Remove elemento (não gera erro se não existir)
s1.clear()        # 🧹 Esvazia o conjunto

# 🔢 Operações entre conjuntos
s2 = {2, 3, 4}
s3 = {3, 4, 5}

print('União (|):', s2 | s3)        # {2, 3, 4, 5}
print('Interseção (&):', s2 & s3)   # {3, 4}
print('Diferença (-):', s2 - s3)    # {2}
print('Dif. Simétrica (^):', s2 ^ s3) # {2, 5}

"""
💡 USOS PRÁTICOS:
1. Remover duplicatas de listas:
   lista = [1, 2, 2, 3]
   sem_duplicatas = list(set(lista))

2. Verificar pertencimento rápido:
   if valor in meu_set:  # Mais rápido que em listas

3. Comparar grupos de elementos

📌 LIMITAÇÕES:
- Não podem conter listas/dicionários (mutáveis)
- Não mantêm ordem de inserção (antes do Python 3.7)
"""

"""
📚 TEORIA DOS CONJUNTOS:
Diagramas de Venn são usados para visualizar:
- União: todos elementos de ambos conjuntos
- Interseção: apenas elementos comuns
- Diferença: elementos exclusivos de um conjunto
- Dif. Simétrica: elementos não compartilhados
"""

# 🆚 EXEMPLO COMPARATIVO
palavras = ["Lucas", "Heitor", "Barbosa", "Lucas"]
unicas = set(palavras)
print(f"Nomes únicos: {unicas}")  # {'Lucas', 'Heitor', 'Barbosa'}