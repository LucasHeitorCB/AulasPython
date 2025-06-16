"""
📦 EMPACOTAMENTO E DESEMPACOTAMENTO EM PYTHON
-------------------------------------------
O desempacotamento permite extrair valores de sequências (listas, tuplas etc.) 
em variáveis individuais de forma concisa.

*_ → Convenção para ignorar valores
*resto → Captura os valores restantes em uma lista
"""

# 🎁 Lista com múltiplos valores
dados = ['Maria', 'Helena', 'Luiz']

# 📦 Desempacotamento com ignoramento de valores
_, _, nome, *resto = dados  
# 📌 _ ignora os 2 primeiros itens (convenção)
# 📌 nome recebe 'Luiz' (3º item)
# 📌 *resto captura o restante (vazio aqui)

print(nome)  # 🖨️ Saída: 'Luiz'

"""
💡 ENTENDENDO CADA PARTE:
1. ['Maria', 'Helena', 'Luiz'] → lista original
2. _, _ → ignora os dois primeiros valores
3. nome → recebe o terceiro valor ('Luiz')
4. *resto → empacota qualquer valor extra (neste caso, vazio)

📌 CASOS COMUNS DE USO:
1. Extrair partes específicas de dados:
   primeiro, *meio, ultimo = [1, 2, 3, 4, 5]

2. Funções que retornam múltiplos valores:
   x, y, z = coordenadas()

3. Processamento de linhas em arquivos:
   cabecalho, *dados = arquivo.readlines()

✨ EXEMPLO PRÁTICO:
lista = [1, 2, 3, 4, 5]
a, b, *c = lista
# a=1, b=2, c=[3, 4, 5]
"""

"""
⚠️ CUIDADOS:
1. Número de variáveis deve bater com itens desempacotados
   (a menos que use *resto)
2. _ é convenção para variáveis descartáveis
3. * só pode ser usado em uma variável por desempacotamento
"""

"""
📚 APRENDIZADOS:
1. Sintaxe básica de desempacotamento
2. Uso de _ para ignorar valores
3. Empacotamento do resto com *
4. Aplicações práticas
"""