# 🔍 Operadores lógicos
# and (e) - Todas as condições precisam ser verdadeiras.
# or (ou) - Pelo menos uma das condições precisa ser verdadeira.
# not (não) - Inverte o valor lógico.

# Exemplo de "and" (todas as condições precisam ser verdadeiras)
print(True and False and True)  # 🚫 False: porque a segunda condição é False
print(True and 0 and True)      # 🚫 0 é falsy, logo o resultado é False

# Exemplo de "or" (pelo menos uma condição precisa ser verdadeira)
print(True or False or True)   # ✅ True: porque a primeira condição é True
print(False or 0 or True)      # ✅ True: porque a última condição é True

# Exemplo de "not" (inverte o valor lógico)
print(not True)  # ❌ False: porque not inverte o valor
print(not False) # ✅ True: porque not inverte o valor

# 🛑 Avaliação de curto-circuito:
# No "and", a expressão é avaliada até encontrar um valor False (curto-circuito).
# No "or", a expressão é avaliada até encontrar um valor True (curto-circuito).






