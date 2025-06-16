"""
🎌 CONCEITO DE FLAG (BANDEIRA) E IDENTIDADE EM PYTHON
----------------------------------------------------
Flags são variáveis booleanas que marcam estados/condições no código.
None é um valor especial que representa a ausência de valor.

Operadores de identidade:
- is → verifica se objetos são os mesmos (identidade)
- is not → verifica se objetos não são os mesmos
"""

# 🏁 Inicializando uma flag e variável de estado
condicao = False          # 🚩 Flag booleana
passou_no_if = None       # 🏷️ Variável de estado (inicialmente sem valor)

# 1️⃣ Primeira estrutura condicional
if condicao:
    passou_no_if = True   # ✅ Marca que passou no if
    print('Faça algo')    # Executa ação condicional
else:
    print('Não faça algo')  # Executa ação alternativa

# 2️⃣ Verificação de estado com 'is'
if passou_no_if is None:  # 🕵️ Verifica identidade (None)
    print('❌ Não passou no if')  # Nunca entrou no primeiro if
else:
    print('✅ Passou no if')     # Entrou no primeiro if

"""
💡 DIFERENÇA ENTRE '==' E 'IS':
- '==' compara VALORES
- 'is' compara IDENTIDADES (se são o mesmo objeto)

📌 EXEMPLO PRÁTICO:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True (mesmos valores)
print(a is b)  # True (mesmo objeto)
print(a == c)  # True (mesmos valores)
print(a is c)  # False (objetos diferentes)

🔍 FUNÇÃO ID():
Mostra o identificador único do objeto:
print(id(a))  # Ex: 140245678945600
print(id(c))  # Ex: 140245678947520 (diferente)
"""

"""
📝 BOAS PRÁTICAS:
1. Use None para inicializar variáveis quando apropriado
2. Prefira 'is' para comparar com None
3. Flags devem ter nomes que indiquem claramente seu propósito
4. Evite usar 'is' para comparação de valores, apenas identidade
"""