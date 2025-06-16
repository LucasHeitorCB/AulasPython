"""
📝 INTERPOLAÇÃO DE STRINGS COM OPERADOR %
-----------------------------------------
A interpolação é uma forma de inserir valores em strings de maneira dinâmica.
O operador % é usado para formatar strings com diferentes tipos de dados:
- %s → String
- %d/%i → Inteiro
- %f → Float
- %x/%X → Hexadecimal (minúsculo/maiúsculo)
"""

# 👤 Dados do exemplo
nome = 'Luiz'  # 🏷️ Variável do tipo string
preco = 1000.95897643  # 💰 Variável do tipo float

# 🧵 Formatação básica com interpolação
variavel = '%s, o preço é R$%.2f' % (nome, preco)  
# 📌 %s substitui pelo nome (string)
# 📌 %.2f substitui pelo preço com 2 casas decimais

print(variavel)  # 🖨️ Saída: "Luiz, o preço é R$1000.96"

# 🔢 Formatação com hexadecimal
print('O hexadecimal de %d é %08X' % (1500, 1500))  
# 📌 %d formata o número inteiro (1500)
# 📌 %08X formata como hexadecimal com 8 dígitos, preenchendo com zeros
#    O 'X' maiúsculo gera letras A-F em maiúsculas (usar 'x' para minúsculas)
#    Saída: "O hexadecimal de 1500 é 000005DC"

"""
💡 DICA EXTRA:
Para formatar números com separador de milhar, pode-se usar:
print('%d' % 1000) → "1000"
print('%.2f' % 1000) → "1000.00"
"""