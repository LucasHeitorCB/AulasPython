"""
🎯 OPERAÇÃO TERNÁRIA EM PYTHON
-------------------------------
A operação ternária permite escrever condicionais em uma única linha:
<valor_se_verdadeiro> if <condição> else <valor_se_falso>
"""

# 🔍 Exemplo básico
condicao = 10 == 11  # False
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)  # 🖨️ 'Outro valor'

# 🔢 Exemplo com números
digito = 9
novo_digito = digito if digito <= 9 else 0  # ✅ Limita a 9
# Equivalente a:
novo_digito = 0 if digito > 9 else digito
print(novo_digito)  # 🖨️ 9

# 🎚️ Ternárias aninhadas (evitar quando possível)
resultado = ('Valor' if False else 
             'Outro valor' if False else 
             'Fim')
print(resultado)  # 🖨️ 'Fim'

"""
💡 BOAS PRÁTICAS:
1. Use para condições simples (1 linha clara)
2. Evite ternárias aninhadas - dificultam a leitura
3. Prefira if/else quando a lógica for complexa

⚠️ CUIDADO COM:
- Ternárias muito longas (dificulta manutenção)
- Múltiplas condições aninhadas
- Legibilidade vs. concisão

✨ ALTERNATIVAS LEGÍVEIS:
"""
# Usando dicionário para mapeamento
mapeamento = {True: 'Valor', False: 'Outro valor'}
print(mapeamento[10 == 10])  # 'Valor'

"""
📌 CASOS DE USO COMUNS:
1. Atribuição condicional simples
2. Retorno condicional em funções lambda
3. Valores padrão para variáveis
4. Filtros em list comprehensions
"""

"""
📚 APRENDIZADOS:
1. Sintaxe básica da operação ternária
2. Quando usar e quando evitar
3. Alternativas para casos complexos
4. Impacto na legibilidade do código
"""