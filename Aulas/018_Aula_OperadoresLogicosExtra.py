# 🔍 Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'

# Exemplos de uso de "in" (verifica se o valor está presente)
print('vio' in nome)  # ✅ True: porque "vio" está presente em "Otávio"
print('zero' in nome) # 🚫 False: porque "zero" não está presente em "Otávio"

# Exemplos de uso de "not in" (verifica se o valor não está presente)
print('vio' not in nome)  # 🚫 False: porque "vio" está presente em "Otávio"
print('zero' not in nome) # ✅ True: porque "zero" não está presente em "Otávio"

# 📝 Entrada do usuário para buscar algo no nome
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

# Condicional para verificar se o valor está ou não presente no nome
if encontrar in nome:
    print(f'{encontrar} está em {nome}')  # ✅ Caso o valor esteja
else:
    print(f'{encontrar} não está em {nome}')  # 🚫 Caso o valor não esteja
