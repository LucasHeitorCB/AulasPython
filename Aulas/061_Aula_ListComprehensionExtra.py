"""
🚀 LIST COMPREHENSION AVANÇADA EM PYTHON
----------------------------------------
Este código demonstra:
1. List comprehension básica para transformação de dados
2. List comprehension com condicionais
3. Desempacotamento de dicionários
4. Formatação de saída para melhor visualização
"""

# 🔄 List comprehension básica (dobrando valores)
numeros = [numero * 2 for numero in range(10)]
print('Números dobrados:', numeros)  # 🖨️ [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 🛒 Dados de produtos originais
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# 💰 Aplicando aumento de 5% apenas em produtos > R$20
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.05, 2)}  # ✏️ Aumento 5%
    if produto['preco'] > 20 else {**produto}  # 🤔 Condicional
    for produto in produtos  # 🔄 Iteração
]

# 🖨️ Exibindo resultados formatados
print('\nProdutos atualizados:')
print(*novos_produtos, sep='\n')  # 📦 Desempacota e separa por linhas

"""
💡 ANÁLISE DO CÓDIGO:
1. {**produto} cria uma cópia do dicionário original
2. round(valor, 2) garante 2 casas decimais para preços
3. A condicional if/else é aplicada a cada item
4. print(*lista, sep='\n') formata a saída verticalmente

📌 EXEMPLOS ADICIONAIS:
"""
# 🏷️ Filtrando produtos caros
produtos_caros = [p for p in produtos if p['preco'] > 20]
print('\nProdutos caros:', produtos_caros)

# 🏷️ Apenas nomes de produtos
nomes = [p['nome'] for p in produtos]
print('Nomes dos produtos:', nomes)

"""
⚠️ CUIDADOS:
1. Evite list comprehensions muito complexas
2. Para transformações muito elaboradas, prefira loops tradicionais
3. Cuidado com mutabilidade ao copiar dicionários

✨ BOAS PRÁTICAS:
1. Use para transformações simples e claras
2. Adicione comentários para lógicas condicionais complexas
3. Formate a saída para melhor legibilidade
4. Documente o propósito da transformação
"""

"""
📚 APRENDIZADOS:
1. Como usar condicionais em list comprehension
2. Técnicas para manipular dicionários
3. Formatação de saída profissional
4. Quando usar vs evitar list comprehension
"""