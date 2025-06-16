"""
📚 CÓPIAS DE DICIONÁRIOS EM PYTHON (SHALLOW COPY vs DEEP COPY)
-----------------------------------------------------------
Este código demonstra a diferença entre cópia superficial (shallow) e profunda (deep) em dicionários.
"""

import copy  # 📦 Módulo necessário para deep copy

# 📍 Dicionário original
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],  # ⚠️ Lista é mutável!
}

# 1️⃣ Shallow Copy (cópia superficial)
d2 = d1.copy()  # 🔄 Cria nova cópia do dicionário, mas não dos elementos internos

# ✏️ Modificando a cópia
d2['c1'] = 1000      # ✅ Altera apenas d2 (int é imutável)
d2['l1'][1] = 999999 # ⚠️ Altera ambas as listas (d1 e d2)!

print('Dicionário original (d1):', d1)
print('Cópia superficial (d2):', d2)

"""
💡 RESULTADO ESPERADO:
d1: {'c1': 1, 'c2': 2, 'l1': [0, 999999, 2]}  # 😱 Lista modificada!
d2: {'c1': 1000, 'c2': 2, 'l1': [0, 999999, 2]}

📌 PROBLEMA DA SHALLOW COPY:
- Apenas o primeiro nível é copiado
- Elementos mutáveis internos são compartilhados
- Modificações em elementos internos afetam ambos

🆚 SOLUÇÃO: DEEP COPY (cópia profunda)
"""
d3 = copy.deepcopy(d1)  # 🌀 Cria cópia completa independente
d3['l1'][0] = 'Lucas'   # ✏️ Modifica apenas d3

print('\nApós deep copy:')
print('Original (d1):', d1)  # 🔄 Permanece inalterado
print('Deep copy (d3):', d3) # 🆕 Modificação isolada

"""
✨ BOAS PRÁTICAS:
1. Use .copy() para dicionários sem estruturas internas complexas
2. Prefira copy.deepcopy() quando houver listas/dicionários aninhados
3. Documente claramente quando compartilhamento é intencional
4. Para dicionários grandes, avalie performance do deepcopy

🔍 DIFERENÇAS CHAVE:
- Shallow copy: rápido, mas compartilha referências internas
- Deep copy: mais lento, mas completamente independente
"""

"""
📚 APRENDIZADOS:
1. Como funcionam cópias superficiais em Python
2. Riscos de compartilhamento não intencional
3. Quando usar deep copy
4. Impacto na manipulação de dados aninhados
"""