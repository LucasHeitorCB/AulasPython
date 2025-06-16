"""
✂️ FATIAMENTO DE STRINGS EM PYTHON
-----------------------------------
O fatiamento (slicing) permite extrair partes de uma string usando índices.
Sintaxe: [início:fim:passo]
- Índices começam em 0
- Valores negativos contam do final
- Omissão de valores usa padrões (início=0, fim=len, passo=1)
"""

variavel = 'Olá mundo'  # 🏷️ String exemplo (9 caracteres)

"""
ÍNDICES POSITIVOS:
 0 1 2 3 4 5 6 7 8
 O l á   m u n d o

ÍNDICES NEGATIVOS:
-9-8-7-6-5-4-3-2-1
"""

# 🔄 Inversão da string
print(variavel[::-1])  
# 📌 [::1] sem passo (padrão)
# 📌 [::-1] passo negativo inverte a string
# Resultado: "odnum álO"

"""
📚 OUTROS EXEMPLOS ÚTEIS:
print(variavel[4:])    # "mundo" (do índice 4 até o fim)
print(variavel[:3])    # "Olá" (do início até índice 2)
print(variavel[2:5])   # "á m" (do índice 2 ao 4)
print(variavel[::2])   # "Oámno" (pulando de 2 em 2)
print(variavel[-5:])   # "mundo" (5 últimos caracteres)
"""

# 📏 FUNÇÃO LEN
print(f'Tamanho: {len(variavel)}')  
# 📌 len() retorna o número de caracteres
# Resultado: "Tamanho: 9" (inclui espaço e acentos)

"""
💡 CURIOSIDADE:
O fatiamento é seguro - índices fora do range não causam erros:
print(variavel[0:100]) → "Olá mundo"
print(variavel[-100:5]) → "Olá m"
"""