nome = 'Ana Clara'
altura = 1.65
peso = 60
imc = peso / (altura ** 2)

# 🧾 Usando f-strings para interpolar variáveis e formatar números
linha_1 = f'{nome} tem {altura:.2f}m de altura,'
linha_2 = f'pesa {peso}kg e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Ana Clara tem 1.65m de altura,
# pesa 60kg e seu IMC é
# 22.04
