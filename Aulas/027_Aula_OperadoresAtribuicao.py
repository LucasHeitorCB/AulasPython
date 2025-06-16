"""
🧮 OPERADORES DE ATRIBUIÇÃO EM PYTHON
--------------------------------------
Operadores que combinam uma operação matemática com atribuição.
São úteis para escrever código mais conciso.

Lista completa:
=   Atribuição simples
+=  Adição e atribuição
-=  Subtração e atribuição
*=  Multiplicação e atribuição
/=  Divisão e atribuição (retorna float)
//= Divisão inteira e atribuição
**= Exponenciação e atribuição
%=  Módulo e atribuição (resto da divisão)
"""

contador = 10  # ⏱️ Inicializando variável

# 🧪 Operação de atribuição com divisão
contador /= 5  # 🔄 Equivalente a: contador = contador / 5
print(contador)  # 🖨️ Resultado: 2.0 (divisão normal retorna float)

"""
📚 EXEMPLOS COM TODOS OPERADORES:

contador = 10
contador += 2    # 12 (10 + 2)
contador -= 3    # 9 (12 - 3)
contador *= 4    # 36 (9 × 4)
contador //= 5   # 7 (36 ÷ 5 como divisão inteira)
contador **= 2   # 49 (7 elevado a 2)
contador %= 10   # 9 (resto de 49 ÷ 10)

💡 DICA IMPORTANTE:
- Para divisão inteira use //
- Para divisão normal (float) use /
- O operador % calcula o resto da divisão
"""

"""
🔍 COMPORTAMENTO EM DIFERENTES TIPOS:
Estes operadores também funcionam com outros tipos:

texto = "Py"
texto += "thon"  # "Python"

lista = [1, 2]
lista += [3, 4]  # [1, 2, 3, 4]

📌 CUIDADO:
A operação depende do tipo do primeiro operando:
x = 10
x += 5.5  # 15.5 (converte para float)
"""

# 🆚 VERSÃO SEM OPERADOR DE ATRIBUIÇÃO
contador = 10
contador = contador / 5  # Equivalente a /=
print(contador)  # Mesmo resultado: 2.0

"""
💼 USO PRÁTICO:
São especialmente úteis em:
- Contadores em loops
- Acumuladores em cálculos
- Construção progressiva de strings/listas
"""