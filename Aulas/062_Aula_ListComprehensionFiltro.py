"""
🚀 LIST COMPREHENSION AVANÇADA COM FILTROS
------------------------------------------
Este código demonstra o uso avançado de list comprehension com:
1. Transformação condicional de dados
2. Filtros complexos
3. Formatação profissional de saída
"""

from pprint import pprint

def p(v):
    """Função auxiliar para impressão formatada"""
    pprint(v, sort_dicts=False, width=40)

# 🛒 Dados de produtos originais
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# 💡 List comprehension com:
# - Transformação condicional (aumento de 5% se preço > 20)
# - Filtro complexo (preço >= 20 E preço com aumento > 10)
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}  # Aumento de 5%
    if produto['preco'] > 20 else {**produto}       # Mantém os demais
    for produto in produtos                         # Itera sobre produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 > 10)  # Filtro
]

print("🏷️ Produtos filtrados e transformados:")
p(novos_produtos)

"""
💡 ANÁLISE DETALHADA:

1. Transformação Condicional:
   - Aplica aumento de 5% apenas se preço > 20
   - Mantém os demais produtos inalterados

2. Filtro Complexo:
   - produto['preco'] >= 20: seleciona produtos com preço mínimo de 20
   - produto['preco'] * 1.05 > 10: garante que mesmo com aumento o preço fique acima de 10

3. Formatação de Saída:
   - pprint mostra a estrutura de dados de forma organizada
   - sort_dicts=False mantém a ordem original dos dicionários
   - width=40 limita a largura da exibição

📌 RESULTADO ESPERADO:
[{'nome': 'p1', 'preco': 20},
 {'nome': 'p3', 'preco': 31.5}]
"""

"""
⚠️ CUIDADOS COM LIST COMPREHENSION COMPLEXA:
1. Pode reduzir a legibilidade do código
2. Difícil depuração quando há erros
3. Pode se tornar ineficiente para grandes datasets

✨ ALTERNATIVAS PARA CÓDIGO COMPLEXO:
1. Usar funções auxiliares
2. Dividir em múltiplas comprehensions
3. Utilizar loops tradicionais quando necessário
"""

"""
📚 APRENDIZADOS:
1. Como combinar transformações e filtros
2. Uso de condições complexas em comprehensions
3. Técnicas profissionais de formatação de saída
4. Quando evitar comprehensions muito complexas
"""