"""
📝 FORMATAÇÃO DE STRINGS COM f-strings (Python 3.6+)
-----------------------------------------
As f-strings oferecem uma forma moderna e poderosa de formatar strings, 
permitindo expressões embutidas dentro de {}.

Principais recursos:
- Alinhamento: > (direita), < (esquerda), ^ (centro)
- Precisão: .<n>f para casas decimais
- Sinal: + (mostra sempre), - (apenas negativos)
- Formatação numérica: , (separador de milhar)
- Conversões: !r (repr()), !s (str()), !a (ascii())
"""

variavel = 'ABC'  # 🏷️ String de exemplo

# 1️⃣ Formatação básica
print(f'{variavel}')  
# 📌 Simples substituição: insere o valor da variável

# 2️⃣ Alinhamentos
print(f'{variavel: >10}')  
# 📌 Alinha à direita em 10 caracteres: "       ABC"

print(f'{variavel: <10}.')  
# 📌 Alinha à esquerda em 10 caracteres: "ABC       ."

print(f'{variavel: ^10}.')  
# 📌 Centraliza em 10 caracteres: "   ABC    ."

# 3️⃣ Formatação numérica avançada
print(f'{1000.4873648123746:0=+10,.1f}')  
# 📌 Formatação completa:
#    - 0= Preenche com zeros
#    - + Mostra sinal sempre
#    - 10 Tamanho total
#    - , Separador de milhar
#    - .1f 1 casa decimal
#    Resultado: "+01,000.5"

# 4️⃣ Hexadecimal
print(f'O hexadecimal de 1500 é {1500:08X}')  
# 📌 Formata como hexadecimal com 8 dígitos e letras maiúsculas
#    Resultado: "O hexadecimal de 1500 é 000005DC"

# 5️⃣ Conversões especiais
print(f'{variavel!r}')  
# 📌 !r chama repr() do objeto: "'ABC'" (inclui aspas)

"""
💡 DICAS EXTRAS:
1. Para porcentagem: f'{0.45:.2%}' → "45.00%"
2. Para notação científica: f'{1000:.2e}' → "1.00e+03"
3. Para preencher com outros caracteres: f'{variavel:*^10}'
"""

# 🆚 Comparação com o método antigo (%)
# As f-strings são:
# - Mais legíveis
# - Mais expressivas
# - Mais performáticas
# - Mais seguras contra erros